// Book: Node.js for DevOps Engineers — Example 33
// src/lib/dirs.js
import os from 'node:os';
import path from 'node:path';

const home = os.homedir();

export const configDir = path.join(
  process.env.XDG_CONFIG_HOME ?? path.join(home, '.config'),
  'kes',
);

export const cacheDir = path.join(
  process.env.XDG_CACHE_HOME ?? path.join(home, '.cache'),
  'kes',
);
