// Book: Node.js for DevOps Engineers — Example 51
// examples/dollar-demo.js
import { $ } from '../src/lib/dollar.js';

const branch = 'feature/new tracking'; // has a space
const files = ['README.md', 'package.json'];

console.log(await $`git rev-parse --short HEAD`);
console.log(await $`git log -1 --format=%an -- ${files}`);
await $`git check-ref-format --branch ${branch}`
  .catch(() => console.log('invalid branch name'));
