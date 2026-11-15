// Book: Node.js for DevOps Engineers — Example 74
// examples/fetch-tour.js
const url = 'https://api.github.com/rate_limit';
const res = await fetch(url, {
  headers: {
    Accept: 'application/vnd.github+json',
    'User-Agent': 'kes/0.3',
  },
  signal: AbortSignal.timeout(5000),
});

console.log(res.status, res.statusText);
console.log(res.headers.get('x-ratelimit-remaining'));
const body = await res.json();
console.log(body.resources.core);
