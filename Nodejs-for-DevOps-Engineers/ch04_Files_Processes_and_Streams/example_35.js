// Book: Node.js for DevOps Engineers — Example 35
// examples/git-info.js
import { run } from '../src/lib/run.js';

const sha = await run('git', [
  'rev-parse', '--short', 'HEAD',
]);
const branch = await run('git', [
  'rev-parse', '--abbrev-ref', 'HEAD',
]);
const dirty = (await run('git', ['status', '--porcelain']))
  .length > 0;

console.log({ sha, branch, dirty });
