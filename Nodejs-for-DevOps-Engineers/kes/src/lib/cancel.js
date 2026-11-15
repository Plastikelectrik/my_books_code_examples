// Ctrl+C cancellation combined with timeouts (Chapter 3).
const controller = new AbortController();
let installed = false;

export function installCancel() {
  if (installed) return;
  installed = true;
  process.once('SIGINT', () => {
    console.error('\ncancelling...');
    controller.abort();
  });
}

export const userSignal = controller.signal;

export function withTimeout(ms) {
  return AbortSignal.any([
    userSignal,
    AbortSignal.timeout(ms),
  ]);
}
