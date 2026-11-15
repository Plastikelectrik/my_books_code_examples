// Book: Node.js for DevOps Engineers — Example 111
// scripts/ci/gha.js
import { appendFile } from 'node:fs/promises';
import { EOL } from 'node:os';

export async function setOutput(name, value) {
  const file = process.env.GITHUB_OUTPUT;
  if (!file) return;
  const delim = `EOF_${crypto.randomUUID()}`;
  await appendFile(file,
    `${name}<<${delim}${EOL}${value}${EOL}${delim}${EOL}`);
}

export async function summary(markdown) {
  const file = process.env.GITHUB_STEP_SUMMARY;
  if (file) await appendFile(file, markdown + EOL);
}

export function annotate(level, message, where = {}) {
  const props = Object.entries(where)
    .map(([k, v]) => `${k}=${v}`).join(',');
  console.log(`::${level} ${props}::${message}`);
}
