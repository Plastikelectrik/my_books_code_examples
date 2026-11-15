// Book: Node.js for DevOps Engineers — Example 03
// scripts/cert-expiry.js
import tls from 'node:tls';

const hosts = process.argv.slice(2);
const WARN_DAYS = 21;

function certInfo(host, port = 443) {
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

const DAY = 24 * 60 * 60 * 1000;
const rows = await Promise.all(
  hosts.map(async (host) => {
    try {
      const expires = await certInfo(host);
      const days = Math.floor((expires - Date.now()) / DAY);
      const state = days < WARN_DAYS ? 'WARN' : 'OK';
      return { host, days, state };
    } catch (err) {
      return { host, days: null, state: 'ERROR' };
    }
  }),
);

console.table(rows);
const bad = rows.some((r) => r.state !== 'OK');
process.exitCode = bad ? 1 : 0;
