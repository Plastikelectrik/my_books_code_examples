// Book: Node.js for DevOps Engineers — Example 29
// examples/fs-basics.js
import {
  readFile, writeFile, mkdir, readdir, stat, rm,
} from 'node:fs/promises';

await mkdir('out/reports', { recursive: true });
await writeFile('out/reports/hello.txt', 'hi\n');

const text = await readFile(
  'out/reports/hello.txt',
  'utf8',
);
console.log(text.trim());

for (const entry of await readdir('out', {
  withFileTypes: true,
  recursive: true,
})) {
  const kind = entry.isDirectory() ? 'dir ' : 'file';
  console.log(kind, entry.parentPath, entry.name);
}

const info = await stat('out/reports/hello.txt');
console.log(`${info.size} bytes, modified ${info.mtime}`);

await rm('out', { recursive: true, force: true });
