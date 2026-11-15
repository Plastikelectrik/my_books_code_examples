import { redact } from '../../config/load.js';

export const meta = {
  name: 'config show',
  summary: 'Print the effective configuration',
  usage: 'kes config show [--profile NAME] [--json]',
  options: {},
};

export async function run(ctx) {
  const safe = redact(ctx.config);
  ctx.out.result(safe, (c) => {
    for (const [k, v] of Object.entries(c)) {
      console.log(`${k.padEnd(14)} ${v}`);
    }
  });
}
