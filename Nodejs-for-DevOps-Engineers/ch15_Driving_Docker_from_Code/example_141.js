// Book: Node.js for DevOps Engineers — Example 141
// examples/docker-version.js
import http from 'node:http';

function dockerGet(path) {
  return new Promise((resolve, reject) => {
    const req = http.request({
      socketPath: '/var/run/docker.sock',
      path,
      method: 'GET',
      timeout: 5000,
    }, (res) => {
      let body = '';
      res.on('data', (c) => (body += c));
      res.on('end', () => resolve(JSON.parse(body)));
    });
    req.on('timeout', () => req.destroy(
      new Error('docker API timeout')));
    req.on('error', reject);
    req.end();
  });
}

const v = await dockerGet('/version');
console.log(`Engine ${v.Version}, API ${v.ApiVersion}`);
