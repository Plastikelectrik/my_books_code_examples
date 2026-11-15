// Book: Node.js for DevOps Engineers — Example 88
// src/fleet/shell-quote.js
export function shq(value) {
  return `'${String(value).replaceAll("'", `'\\''`)}'`;
}
