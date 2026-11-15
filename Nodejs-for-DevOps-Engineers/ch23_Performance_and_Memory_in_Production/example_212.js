// Book: Node.js for DevOps Engineers — Example 212
// src/diagnostics/signals.js
import { captureCpuProfile } from './cpu-profile.js';
import { logger } from '../lib/logger.js';

let busy = false;
process.on('SIGUSR2', async () => {
  if (busy) return;
  busy = true;
  logger.warn('cpu profile started (30s)');
  try {
    const file = await captureCpuProfile(30);
    logger.warn({ file }, 'cpu profile written');
  } finally {
    busy = false;
  }
});
