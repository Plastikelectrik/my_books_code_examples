// Book: Node.js for DevOps Engineers — Example 02
// src/version.js
import { readFile } from 'node:fs/promises';

const pkgUrl = new URL('../package.json', import.meta.url);
const pkg = JSON.parse(await readFile(pkgUrl, 'utf8'));

console.log(`kes ${pkg.version}`);
console.log(`node ${process.version}`);
console.log(`platform ${process.platform}`);
