// Book: Node.js for DevOps Engineers — Example 76
// src/lib/oauth.js
export function clientCredentials({ tokenUrl, id, secret,
  scope }) {
  let cached = null;

  return async function getToken() {
    const soon = Date.now() + 60_000;
    if (cached && cached.expiresAt > soon) {
      return cached.token;
    }
    const res = await fetch(tokenUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: id,
        client_secret: secret,
        ...(scope ? { scope } : {}),
      }),
      signal: AbortSignal.timeout(10_000),
    });
    if (!res.ok) {
      throw new Error(`token: HTTP ${res.status}`);
    }
    const json = await res.json();
    cached = {
      token: json.access_token,
      expiresAt: Date.now() + json.expires_in * 1000,
    };
    return cached.token;
  };
}
