// Book: Node.js for DevOps Engineers — Example 56
// examples/parse-demo.js
import { parseArgs } from 'node:util';

const { values, positionals } = parseArgs({
  allowPositionals: true,
  options: {
    env: { type: 'string', short: 'e', default: 'staging' },
    tag: { type: 'string', multiple: true },
    json: { type: 'boolean', default: false },
    verbose: { type: 'boolean', short: 'v' },
  },
});

console.log({ values, positionals });
