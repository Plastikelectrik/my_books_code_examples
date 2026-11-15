// Parse `df -P /` output (Chapter 9 exercise).
export function parseDf(stdout) {
  const line = stdout.trim().split('\n')[1] ?? '';
  const pct = Number(line.trim().split(/\s+/)[4]
    ?.replace('%', ''));
  return Number.isFinite(pct) ? pct : null;
}
