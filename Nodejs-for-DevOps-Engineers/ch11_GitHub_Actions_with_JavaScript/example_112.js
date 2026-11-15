// Book: Node.js for DevOps Engineers — Example 112
// scripts/ci/check-manifests.js
import { glob, readFile } from 'node:fs/promises';
import { parseAllDocuments } from 'yaml';
import { annotate, summary } from './gha.js';

let problems = 0;
for await (const file of glob('deploy/**/*.yaml')) {
  const text = await readFile(file, 'utf8');
  const docs = parseAllDocuments(text);
  for (const doc of docs) {
    const kind = doc.get('kind');
    const limits = doc.getIn(['spec', 'template', 'spec',
      'containers', 0, 'resources', 'limits']);
    if (kind === 'Deployment' && !limits) {
      annotate('error', 'container has no resource limits',
        { file });
      problems++;
    }
  }
}
await summary(
  `### Manifest check\n\n${problems} problem(s)`);
process.exitCode = problems ? 1 : 0;
