import { readFile } from 'node:fs/promises';

export const meta = {
  name: 'version',
  summary: 'Show kes and Node.js versions',
  usage: 'kes version [--json]',
  options: {},
};

export async function run(ctx) {
  const pkgUrl = new URL('../../../package.json',
    import.meta.url);
  const pkg = JSON.parse(await readFile(pkgUrl, 'utf8'));
  const info = {
    kes: pkg.version,
    node: process.version,
    platform: process.platform,
  };
  ctx.out.result(info, (i) => {
    for (const [k, v] of Object.entries(i)) {
      console.log(`${k} ${v}`);
    }
  });
}
