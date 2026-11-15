// Book: Node.js for DevOps Engineers — Example 20
// src/lib/cancel.js
const controller = new AbortController();

process.once('SIGINT', () => {
  console.error('\ncancelling...');
  controller.abort();
});

export const userSignal = controller.signal;

export function withTimeout(ms) {
  return AbortSignal.any([
    userSignal,
    AbortSignal.timeout(ms),
  ]);
}
