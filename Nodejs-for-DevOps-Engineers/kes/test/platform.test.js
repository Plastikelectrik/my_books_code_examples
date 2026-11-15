import { test } from 'node:test';
import assert from 'node:assert/strict';
import { rolloutState } from '../src/kube/rollout.js';
import { auditDeployment } from '../src/kube/audit.js';
import { planCleanup } from '../src/docker/cleanup-plan.js';
import { createState } from '../src/alerts/state.js';
import { fromPrometheus, formatAlert }
  from '../src/alerts/model.js';

test('rolloutState', () => {
  const d = (status) => ({ metadata: { generation: 2 },
    spec: { replicas: 3 }, status });
  assert.equal(rolloutState(d({ observedGeneration: 2,
    replicas: 3, updatedReplicas: 3,
    availableReplicas: 3 })).ok, true);
  assert.equal(rolloutState(d({ observedGeneration: 1,
    replicas: 3, updatedReplicas: 3,
    availableReplicas: 3 })).done, false);
  const failed = rolloutState(d({ conditions: [{
    type: 'Progressing', reason: 'ProgressDeadlineExceeded',
    message: 'too slow' }] }));
  assert.deepEqual([failed.done, failed.ok], [true, false]);
});

test('auditDeployment lists every failed check', () => {
  const dep = { spec: { template: { spec: { containers: [
    { name: 'app', image: 'nginx:latest' }] } } } };
  const f = auditDeployment(dep);
  assert.equal(f.length, 7);
  assert.ok(f.includes('app: image pinned (no :latest)'));
});

test('planCleanup', () => {
  const HOUR = 3_600_000;
  const now = 1000 * HOUR;
  const actions = planCleanup({
    containers: [
      { Id: 'old', State: 'exited', finishedAt: now - 48 * HOUR },
      { Id: 'new', State: 'exited', finishedAt: now - HOUR },
      { Id: 'exp', State: 'running', finishedAt: 0,
        Labels: { 'com.kestrel.expires': '1970-01-01' } },
    ],
    images: [{ Id: 'i1', RepoTags: [] },
      { Id: 'i2', RepoTags: ['a:1'] }],
  }, { now });
  assert.deepEqual(actions.map((a) => a.id),
    ['old', 'exp', 'i1']);
});

test('alert state: notify, count, remind, resolve', () => {
  const s = createState();
  const alert = fromPrometheus({ status: 'firing',
    labels: { alertname: 'HighErrors', service: 'orders',
      severity: 'critical' },
    annotations: { summary: 'Errors above 2%' } });
  const t0 = Date.parse('2026-01-01T00:00:00Z');
  let d = s.decide(alert, t0);
  assert.equal(d.action, 'notify');
  s.record(alert, d, t0);
  d = s.decide(alert, t0 + 60_000);
  assert.equal(d.action, 'count');
  s.record(alert, d, t0 + 60_000);
  assert.equal(s.decide(alert, t0 + 5 * 3_600_000).action,
    'remind');
  assert.equal(s.decide({ ...alert, status: 'resolved' },
    t0).action, 'resolve');
  assert.match(formatAlert(alert), /CRITICAL: Errors above 2%/);
});
