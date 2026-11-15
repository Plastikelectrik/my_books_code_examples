// Book: Node.js for DevOps Engineers — Example 31
// examples/bump-replicas.js
import { readFile, writeFile } from 'node:fs/promises';
import { parseDocument } from 'yaml';

const file = 'deploy/tracking.yaml';
const doc = parseDocument(await readFile(file, 'utf8'));

const current = doc.getIn(['spec', 'replicas']);
doc.setIn(['spec', 'replicas'], current + 1);

await writeFile(file, doc.toString());
console.log(`replicas ${current} -> ${current + 1}`);
