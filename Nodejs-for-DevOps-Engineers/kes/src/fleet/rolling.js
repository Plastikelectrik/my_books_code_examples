// Rolling execution with health gates and a failure budget (Chapter 9).
export async function rolling(hosts, task, opts) {
  const {
    batchSizes = [1, 5, 10],
    maxFailures = 1,
    healthCheck,
    log = console.error,
  } = opts;

  const results = [];
  let failures = 0;
  let index = 0;
  let b = 0;

  while (index < hosts.length) {
    const last = batchSizes.length - 1;
    const size = batchSizes[Math.min(b, last)];
    const batch = hosts.slice(index, index + size);
    const names = batch.map((h) => h.name).join(', ');
    log(`batch ${b + 1}: ${names}`);

    const batchResults = await Promise.all(batch.map(task));
    for (const r of batchResults) {
      results.push(r);
      if (!r.ok) failures++;
    }
    if (healthCheck) {
      const healthy = await healthCheck(batch);
      if (!healthy) failures++;
    }
    if (failures >= maxFailures) {
      log(`stopping: ${failures} failure(s)`);
      return { completed: false, results, failures };
    }
    index += size;
    b++;
  }
  return { completed: true, results, failures };
}
