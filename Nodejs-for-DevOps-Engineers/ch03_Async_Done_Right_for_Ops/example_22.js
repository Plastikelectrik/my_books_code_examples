// Book: Node.js for DevOps Engineers — Example 22
// src/lib/timeout.js
export function timeout(promise, ms, label = 'op') {
  let timer;
  const limit = new Promise((_, reject) => {
    timer = setTimeout(
      () => reject(new Error(`${label} timed out`)),
      ms,
    );
  });
  return Promise.race([promise, limit]).finally(() =>
    clearTimeout(timer),
  );
}
