// Book: Node.js for DevOps Engineers — Example 63
// src/lib/spinner.js
const FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧'];

export function spinner(text) {
  if (!process.stderr.isTTY) {
    console.error(text);
    return {
      stop: (final) => final && console.error(final),
    };
  }
  let i = 0;
  const timer = setInterval(() => {
    process.stderr.write(`\r${FRAMES[i++ % 8]} ${text}`);
  }, 80);
  return {
    stop(final = '') {
      clearInterval(timer);
      process.stderr.write(`\r\x1b[K${final}\n`);
    },
  };
}
