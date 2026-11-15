// Book: Node.js for DevOps Engineers — Example 211
// src/diagnostics/cpu-profile.js
import { Session } from 'node:inspector/promises';
import { writeFile } from 'node:fs/promises';
import { setTimeout as sleep } from 'node:timers/promises';

export async function captureCpuProfile(seconds = 30) {
  const session = new Session();
  session.connect();
  try {
    await session.post('Profiler.enable');
    await session.post('Profiler.start');
    await sleep(seconds * 1000);
    const { profile } = await session.post('Profiler.stop');
    const file = `/tmp/cpu-${process.pid}-${Date.now()}` +
      '.cpuprofile';
    await writeFile(file, JSON.stringify(profile));
    return file;
  } finally {
    session.disconnect();
  }
}
