// Book: Node.js for DevOps Engineers — Example 40
// examples/count-status.js
import { createReadStream } from 'node:fs';
import { createInterface } from 'node:readline';

const counts = new Map();
const lines = createInterface({
  input: createReadStream(process.argv[2]),
  crlfDelay: Infinity,
});

for await (const line of lines) {
  const match = line.match(/" (\d{3}) /);
  if (!match) continue;
  const code = match[1];
  counts.set(code, (counts.get(code) ?? 0) + 1);
}

const sorted = [...counts].sort((a, b) => b[1] - a[1]);
for (const [code, n] of sorted) {
  console.log(code, n);
}
