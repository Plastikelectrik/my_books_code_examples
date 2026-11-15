// Quote a value as one POSIX shell word (Chapter 9).
export function shq(value) {
  return `'${String(value).replaceAll("'", `'\\''`)}'`;
}
