// Book: Node.js for DevOps Engineers — Example 121
// src/commands/release.js
import { readFile, writeFile } from 'node:fs/promises';
import semver from 'semver';
import { run } from '../lib/run.js';
import { lastTag, commitsSince } from '../release/git.js';
import { parseCommit, nextBump } from '../release/parse.js';
import { renderNotes } from '../release/notes.js';

export const meta = {
  name: 'release',
  summary: 'Version, tag and record a release',
  usage: 'kes release [--dry-run]',
  options: { 'dry-run': { type: 'boolean' } },
};

export async function run_({ values, out }) {
  const tag = await lastTag();
  const commits = (await commitsSince(tag))
    .map(parseCommit);
  const bump = nextBump(commits);
  if (!bump) {
    const since = tag ?? 'start';
    out.info(`no releasable changes since ${since}`);
    return;
  }

  const pkg = JSON.parse(
    await readFile('package.json', 'utf8'));
  const version = semver.inc(pkg.version, bump);
  const date = new Date().toISOString().slice(0, 10);
  const notes = renderNotes(version, commits, {
    repoUrl: 'https://github.com/kestrel/kes', date,
  });

  out.info(`${pkg.version} -> ${version} (${bump})`);
  if (values['dry-run']) {
    console.log(notes);
    return;
  }

  pkg.version = version;
  await writeFile('package.json',
    JSON.stringify(pkg, null, 2) + '\n');
  await prependChangelog(notes);
  await run('git', ['add', 'package.json', 'CHANGELOG.md']);
  await run('git', ['commit', '-m',
    `chore(release): v${version}`]);
  await run('git', ['tag', '-a', `v${version}`,
    '-m', `v${version}`]);
  out.result({ version, bump }, () =>
    console.log(`tagged v${version}`));
}

export { run_ as run };

async function prependChangelog(notes) {
  let old = '';
  try {
    old = await readFile('CHANGELOG.md', 'utf8');
  } catch {}
  const header = '# Changelog\n\n';
  const rest = old.replace(header, '');
  const body = header + notes + '\n' + rest;
  await writeFile('CHANGELOG.md', body);
}
