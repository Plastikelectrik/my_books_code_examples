// Which registry images may be deleted (Chapter 10).
const DAY = 86_400_000;
const RELEASE = /^v\d+\.\d+\.\d+$/;
const isProtected = (t) =>
  t === 'latest' || RELEASE.test(t);

export function selectForDeletion(images, opts) {
  const { keepLatest = 10, olderThanDays = 30, now } = opts;
  const cutoff = now - olderThanDays * DAY;

  const byRepo = Map.groupBy(images, (img) => img.repo);
  const doomed = [];

  for (const list of byRepo.values()) {
    const sorted = list.toSorted(
      (a, b) => b.pushedAt - a.pushedAt);
    for (const [i, img] of sorted.entries()) {
      const protectedTag = img.tags.some(isProtected);
      if (i < keepLatest || protectedTag) continue;
      if (img.pushedAt < cutoff) doomed.push(img);
    }
  }
  return doomed;
}
