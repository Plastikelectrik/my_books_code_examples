// Book: Node.js for DevOps Engineers — Example 67
// src/commands/config/show.js
export const meta = {
  name: 'config show',
  summary: 'Print the effective configuration',
  usage: 'kes config show [--json]',
  options: {},
};

export async function run({ out, config }) {
  const safe = redact(config);
  out.result(safe, (c) => {
    for (const [k, v] of Object.entries(c)) {
      console.log(`${k.padEnd(14)} ${v}`);
    }
  });
}

function redact(config) {
  const copy = { ...config };
  for (const key of Object.keys(copy)) {
    if (/token|secret|password|webhook/i.test(key)) {
      copy[key] = copy[key] ? '***' : copy[key];
    }
  }
  return copy;
}
