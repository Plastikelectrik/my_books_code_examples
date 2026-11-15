// Book: Node.js for DevOps Engineers — Example 12
// scripts/find-manifests.js
import { glob } from 'node:fs/promises';

for await (const file of glob('deploy/**/*.yaml')) {
  console.log(file);
}
