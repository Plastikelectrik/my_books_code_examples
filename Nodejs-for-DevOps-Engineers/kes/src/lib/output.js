// Human output on stdout, diagnostics on stderr, JSON on demand (Chapter 6).
import { styleText } from 'node:util';

export function createOutput({ json = false, verbose = false } = {}) {
  const isTTY = process.stdout.isTTY;
  return {
    json,
    result(data, render) {
      if (json) {
        process.stdout.write(JSON.stringify(data, null, 2));
        process.stdout.write('\n');
      } else {
        render(data);
      }
    },
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
