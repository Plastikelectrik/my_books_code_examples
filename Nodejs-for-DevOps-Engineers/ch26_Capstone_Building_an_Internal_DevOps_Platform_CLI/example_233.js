// Book: Node.js for DevOps Engineers — Example 233
// scripts/gen-docs.js
import { writeFile, mkdir } from 'node:fs/promises';
import { GROUPS } from '../src/commands/index.js';

const FENCE = '`'.repeat(3); // Markdown code fence

await mkdir('docs/commands', { recursive: true });
for (const group of GROUPS) {
  const lines = [`# ${group.name}`, '',
    `Owner: ${group.owner}`, ''];
  for (const [name, load] of Object.entries(
    group.commands)) {
    const { meta } = await load();
    lines.push(`## kes ${name}`, '', meta.summary, '',
      FENCE, meta.usage, FENCE, '');
    for (const [opt, o] of Object.entries(
      meta.options ?? {})) {
      lines.push(`- \`--${opt}\`: ${o.description ?? ''}`);
    }
    lines.push('');
  }
  await writeFile(`docs/commands/${group.name}.md`,
    lines.join('\n'));
}
