// Book: Node.js for DevOps Engineers — Example 04
// src/lib/paths.js
import { fileURLToPath } from 'node:url';
import path from 'node:path';

export const here = (metaUrl) =>
  path.dirname(fileURLToPath(metaUrl));

export const fromRoot = (...parts) =>
  path.join(here(import.meta.url), '..', '..', ...parts);
