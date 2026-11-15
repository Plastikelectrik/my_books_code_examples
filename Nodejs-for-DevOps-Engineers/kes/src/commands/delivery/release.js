import semver from 'semver';
import { lastTag, commitsSince } from '../../release/git.js';
import { parseCommit, nextBump } from '../../release/parse.js';
import { renderNotes } from '../../release/notes.js';
import { run as runCmd } from '../../lib/run.js';

export const meta = {
  name: 'release',
  summary: 'Work out the next version and release notes ' +
    'from Conventional Commits',
  usage: 'kes release [--repo-url URL] [--tag] [--json]',
  options: {
    'repo-url': { type: 'string',
      default: 'https://github.com/kestrel/app',
      description: 'Used for commit links' },
    tag: { type: 'boolean', default: false,
      description: 'Create the annotated git tag' },
  },
};

export async function run(ctx, { values }) {
  const tag = await lastTag();
  const current = tag ? tag.slice(1) : '0.0.0';
  const commits = (await commitsSince(tag)).map(parseCommit);
  const bump = nextBump(commits);
  if (!bump) {
    return ctx.out.result({ current, next: null },
      () => console.log(`nothing to release since ${
        tag ?? 'the first commit'}`));
  }
  const next = semver.inc(current, bump);
  const date = new Date().toISOString().slice(0, 10);
  const notes = renderNotes(`v${next}`, commits,
    { repoUrl: values['repo-url'], date });

  ctx.out.result({ current, bump, next, notes },
    (r) => {
      ctx.out.info(`${r.current} -> ${r.next} (${r.bump})`);
      console.log(r.notes);
    });
  if (values.tag) {
    await runCmd('git', ['tag', '-a', `v${next}`,
      '-m', `Release v${next}`]);
    ctx.out.info(`created tag v${next} ` +
      '(push it with git push --follow-tags)');
  }
}
