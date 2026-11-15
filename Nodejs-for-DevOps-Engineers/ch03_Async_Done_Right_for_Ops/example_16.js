// Book: Node.js for DevOps Engineers — Example 16
// examples/promise-basics.js
async function getStatus(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

try {
  const status = await getStatus(
    'https://api.example.com/status',
  );
  console.log(status);
} catch (err) {
  console.error('status check failed:', err.message);
  process.exitCode = 1;
}
