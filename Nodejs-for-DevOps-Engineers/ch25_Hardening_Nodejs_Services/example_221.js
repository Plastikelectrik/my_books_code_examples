// Book: Node.js for DevOps Engineers — Example 221
// src/http/errors.js
export function sendError(res, err, log) {
  const status = err.status ?? 500;
  const expose = status < 500;
  log.error({ err, status }, 'request failed');
  res.writeHead(status, {
    'Content-Type': 'application/json',
  }).end(JSON.stringify({
    error: expose ? err.message : 'internal error',
    requestId: res.getHeader('x-request-id'),
  }));
}
