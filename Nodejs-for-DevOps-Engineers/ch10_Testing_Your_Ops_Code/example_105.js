// Book: Node.js for DevOps Engineers — Example 105
// test/helpers/fake-bin.js
import {
  mkdtemp, writeFile, chmod,
} from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

export async function fakeBin(name, script) {
  const dir = await mkdtemp(path.join(tmpdir(), 'bin-'));
  const file = path.join(dir, name);
  await writeFile(file, `#!/usr/bin/env node\n${script}`);
  await chmod(file, 0o755);
  return {
    dir,
    env: {
      ...process.env,
      PATH: `${dir}${path.delimiter}${process.env.PATH}`,
    },
  };
}
