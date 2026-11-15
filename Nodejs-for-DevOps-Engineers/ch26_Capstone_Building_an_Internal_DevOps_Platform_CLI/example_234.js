// Book: Node.js for DevOps Engineers — Example 234
// src/lib/min-version.js
import semver from 'semver';
import { CliError } from './errors.js';

export function checkMinVersion(current, required) {
  if (required && semver.lt(current, required)) {
    throw new CliError(
      `kes ${current} is too old; ` +
      `${required} or newer is required. ` +
      'Run: npm install -g @kestrel/kes',
      { code: 2 });
  }
}
