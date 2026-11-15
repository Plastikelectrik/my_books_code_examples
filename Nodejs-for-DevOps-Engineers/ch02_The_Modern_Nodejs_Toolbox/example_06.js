// Book: Node.js for DevOps Engineers — Example 06
// scripts/whoami.js
const res = await fetch('https://api.github.com/user', {
  headers: {
    Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
  },
});
if (!res.ok) {
  console.error(`GitHub said ${res.status}`);
  process.exit(1);
}
const user = await res.json();
console.log(user.login);
