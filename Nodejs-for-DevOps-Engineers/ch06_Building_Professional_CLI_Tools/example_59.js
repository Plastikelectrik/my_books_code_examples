// Book: Node.js for DevOps Engineers — Example 59
// src/lib/output.js
import { styleText } from 'node:util';

export function createOutput({ json, verbose }) {
  const isTTY = process.stdout.isTTY;
  return {
    json,
    // final result of the command
    result(data, render) {
      if (json) {
        process.stdout.write(JSON.stringify(data, null, 2));
        process.stdout.write('\n');
      } else {
        render(data);
      }
    },
    // progress and diagnostics: always stderr
    info(msg) {
      if (!json) console.error(msg);
    },
    debug(msg) {
      if (verbose) console.error(styleText('gray', msg));
    },
    ok: (m) => isTTY
      ? styleText('green', `✔ ${m}`)
      : `OK ${m}`,
    bad: (m) => isTTY
      ? styleText('red', `✖ ${m}`)
      : `FAIL ${m}`,
  };
}
