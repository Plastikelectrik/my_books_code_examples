// Write a file atomically: temp file + rename (Chapter 4).
import { writeFile, rename, rm, mkdir } from 'node:fs/promises';
import { randomBytes } from 'node:crypto';
import path from 'node:path';

export async function writeAtomic(file, data) {
  const dir = path.dirname(file);
  await mkdir(dir, { recursive: true });
  const suffix = randomBytes(4).toString('hex');
  const name = `.${path.basename(file)}.${suffix}`;
  const tmp = path.join(dir, name);
  try {
    await writeFile(tmp, data, { flush: true });
    await rename(tmp, file);
  } catch (err) {
    await rm(tmp, { force: true });
    throw err;
  }
}
