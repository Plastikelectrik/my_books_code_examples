// Book: Node.js for DevOps Engineers — Example 223
// src/http/body.js
export async function readJsonBody(req, limit = 1_000_000) {
  const declared = Number(req.headers['content-length']);
  if (declared > limit) throw httpError(413, 'too large');

  let size = 0;
  const chunks = [];
  for await (const chunk of req) {
    size += chunk.length;
    if (size > limit) throw httpError(413, 'too large');
    chunks.push(chunk);
  }
  try {
    const text = Buffer.concat(chunks).toString('utf8');
    return JSON.parse(text);
  } catch {
    throw httpError(400, 'invalid JSON');
  }
}

function httpError(status, message) {
  return Object.assign(new Error(message), { status });
}
