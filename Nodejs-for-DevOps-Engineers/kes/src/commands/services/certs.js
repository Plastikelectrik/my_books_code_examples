import tls from 'node:tls';
import { readStdin } from '../../lib/stdin.js';
import { daysUntil } from '../../lib/days.js';
import { mapLimit } from '../../lib/pool.js';
import { CliError } from '../../lib/errors.js';

export const meta = {
  name: 'certs check',
  summary: 'Check TLS certificate expiry of hosts',
  usage: 'kes certs check HOST... [--warn-days N] [--json]',
  options: {
    'warn-days': { type: 'string', default: '21',
      description: 'Warn when fewer days remain' },
  },
};

export function certExpiry(host, port = 443) {
  return new Promise((resolve, reject) => {
    const socket = tls.connect(
      { host, port, servername: host, timeout: 5000 },
      () => {
        const cert = socket.getPeerCertificate();
        socket.end();
        resolve(new Date(cert.valid_to));
      },
    );
    socket.on('timeout', () => {
      socket.destroy();
      reject(new Error('timeout'));
    });
    socket.on('error', reject);
  });
}

export async function run(ctx, { values, positionals },
  deps = { certExpiry }) {
  const warnDays = Number(values['warn-days']);
  if (!Number.isInteger(warnDays) || warnDays < 0) {
    throw new CliError(
      `invalid --warn-days: ${values['warn-days']}`,
      { code: 2 });
  }
  const hosts = positionals.length
    ? positionals
    : (await readStdin()).split(/\s+/).filter(Boolean);
  if (!hosts.length) {
    throw new CliError('give hosts as arguments or on stdin',
      { code: 2 });
  }

  const rows = await mapLimit(hosts, 8, async (host) => {
    try {
      const expires = await deps.certExpiry(host);
      const days = daysUntil(expires);
      const state = days < warnDays ? 'WARN' : 'OK';
      return { host, days, state };
    } catch {
      return { host, days: null, state: 'ERROR' };
    }
  });

  ctx.out.result(rows, (r) => {
    for (const row of r) {
      const line = `${row.host.padEnd(28)} ` +
        `${row.days ?? '-'} days`;
      console.log(row.state === 'OK'
        ? ctx.out.ok(line)
        : ctx.out.bad(`${line} (${row.state})`));
    }
  });
  if (rows.some((r) => r.state !== 'OK')) {
    process.exitCode = 1;
  }
}
