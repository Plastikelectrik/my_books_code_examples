import { test } from 'node:test';
import assert from 'node:assert/strict';
import { planDeploy } from '../src/deploy/plan.js';
import { executePlan } from '../src/deploy/execute.js';
import { analyse, decide } from '../src/canary/analysis.js';
import { runCanary } from '../src/canary/controller.js';
import { memoryRouter } from '../src/canary/traffic.js';
import { parseCommit, nextBump } from '../src/release/parse.js';
import { renderNotes } from '../src/release/notes.js';
import { imageTags } from '../src/release/image-tags.js';
import { selectForDeletion }
  from '../src/registry/select-old.js';

const svc = {
  name: 'orders-api',
  runtime: { kind: 'kubernetes', namespace: 'checkout',
    deployment: 'orders-api', container: 'app' },
  deploy: { strategy: 'canary' },
};

test('planDeploy builds the four steps', () => {
  const p = planDeploy({ svc, env: 'staging', sha: 'abc1234',
    registry: 'r.example.com' });
  assert.equal(p.image, 'r.example.com/orders-api:abc1234');
  assert.equal(p.steps.length, 4);
  assert.deepEqual(p.steps[2][1].slice(0, 4),
    ['--context', 'staging', '-n', 'checkout']);
});

test('planDeploy rejects bad input', () => {
  assert.throws(() => planDeploy({ svc, env: 'qa',
    sha: 'abc1234', registry: 'r' }), /environment/);
  assert.throws(() => planDeploy({ svc, env: 'staging',
    sha: 'HEAD; rm -rf /', registry: 'r' }), /sha/);
});

test('executePlan only runs commands with dryRun false',
  async () => {
    const plan = planDeploy({ svc, env: 'staging',
      sha: 'abc1234', registry: 'r' });
    const ran = [];
    const runner = async (cmd) => { ran.push(cmd); };
    await executePlan(plan, { runner, log: () => {} });
    assert.equal(ran.length, 0);
    await executePlan(plan, { runner, dryRun: false,
      log: () => {} });
    assert.deepEqual(ran,
      ['docker', 'docker', 'kubectl', 'kubectl']);
  });

const good = { requests: 900, errorRate: 0.001, p95Ms: 100,
  p99Ms: 200 };

test('canary analysis', () => {
  assert.equal(decide(analyse(good, good)), 'promote');
  assert.equal(decide(analyse({ ...good, errorRate: 0.05 },
    good)), 'rollback');
  assert.equal(decide(analyse({ ...good, p95Ms: 150 }, good)),
    'rollback');
  assert.equal(decide(analyse({ ...good, requests: 50 },
    good)), 'hold');
});

test('runCanary promotes or rolls back', async () => {
  const opts = { service: 's', stable: 'a', canary: 'b',
    wait: async () => {}, log: () => {} };
  const r1 = memoryRouter();
  const ok = await runCanary({ ...opts, router: r1,
    snapshot: async () => good });
  assert.equal(ok.result, 'promoted');
  assert.deepEqual(r1.history, [5, 25, 50, 100]);

  const r2 = memoryRouter();
  const bad = await runCanary({ ...opts, router: r2,
    snapshot: async (s, v) => v === 'b'
      ? { ...good, errorRate: 0.2 } : good });
  assert.equal(bad.result, 'rolled-back');
  assert.deepEqual(r2.history, [5, 0]);
});

test('conventional commits decide the bump', () => {
  const c = (subject, body) =>
    parseCommit({ hash: 'a'.repeat(40), subject, body });
  assert.equal(nextBump([c('fix: x')]), 'patch');
  assert.equal(nextBump([c('fix: x'), c('feat: y')]), 'minor');
  assert.equal(nextBump([c('feat!: drop v1')]), 'major');
  assert.equal(nextBump([c('feat: y',
    'BREAKING CHANGE: config renamed')]), 'major');
  assert.equal(nextBump([c('chore: deps')]), null);
  const notes = renderNotes('v2.0.0',
    [c('feat(api)!: new auth')],
    { repoUrl: 'https://x', date: '2026-01-01' });
  assert.match(notes, /Breaking changes/);
  assert.match(notes, /\*\*api:\*\* new auth/);
});

test('imageTags adds semver aliases', () => {
  assert.deepEqual(imageTags({ registry: 'r', name: 'n',
    sha: 'abc', version: '1.4.2' }),
  ['r/n:abc', 'r/n:1.4.2', 'r/n:1.4', 'r/n:1']);
});

test('registry cleanup keeps recent and release tags', () => {
  const DAY = 86_400_000;
  const now = 100 * DAY;
  const images = Array.from({ length: 15 }, (_, i) => ({
    repo: 'orders', tags: [i === 14 ? 'v1.0.0' : `sha${i}`],
    pushedAt: now - (i + 25) * DAY,
  }));
  const doomed = selectForDeletion(images,
    { keepLatest: 10, olderThanDays: 30, now });
  assert.deepEqual(doomed.map((d) => d.tags[0]),
    ['sha10', 'sha11', 'sha12', 'sha13']);
});
