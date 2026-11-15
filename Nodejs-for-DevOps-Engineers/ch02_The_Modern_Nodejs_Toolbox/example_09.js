// Book: Node.js for DevOps Engineers — Example 09
// src/config/load-env.js
import { existsSync } from 'node:fs';

if (existsSync('.env.local')) {
  process.loadEnvFile('.env.local');
}
