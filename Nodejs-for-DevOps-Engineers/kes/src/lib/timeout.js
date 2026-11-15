// Put a deadline on any promise (Chapter 3).
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
