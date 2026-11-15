// Book: Node.js for DevOps Engineers — Example 117
// scripts/ci/check-title.js
const TYPES = ['feat', 'fix', 'docs', 'refactor', 'perf',
  'test', 'chore', 'ci', 'build', 'revert'];
const pattern = new RegExp(
  `^(${TYPES.join('|')})(\\([a-z0-9-]+\\))?!?: .{3,}`);

const title = process.argv[2] ?? '';
if (!pattern.test(title)) {
  console.error(`::error::PR title must follow ` +
    `Conventional Commits, e.g. "fix(deploy): ..."`);
  process.exit(1);
}
console.log('title OK');
