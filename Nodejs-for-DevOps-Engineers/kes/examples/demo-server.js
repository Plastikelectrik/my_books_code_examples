// A tiny local server so "kes health" has something to check.
// The inventory service answers 503 on purpose.
import http from 'node:http';

const server = http.createServer((req, res) => {
  const sick = req.url.startsWith('/inventory');
  res.writeHead(sick ? 503 : 200,
    { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ ok: !sick }));
});

server.listen(8080, '127.0.0.1', () => {
  console.log('demo server on http://127.0.0.1:8080');
});
