// Book: Node.js for DevOps Engineers — Example 225
// scripts/ci/node-eol-check.js
const EOL = {
  20: '2026-04-30', 22: '2027-04-30',
  24: '2028-04-30', 26: '2029-04-30',
};
const major = Number(process.versions.node.split('.')[0]);
const eol = EOL[major];
if (!eol) {
  console.log(`::warning::unknown Node.js ${major}`);
} else {
  const days = (Date.parse(eol) - Date.now()) / 86_400_000;
  if (days < 0) {
    console.log(`::error::Node.js ${major} is end-of-life`);
    process.exitCode = 1;
  } else if (days < 120) {
    console.log(`::warning::Node.js ${major} EOL in ` +
      `${Math.round(days)} days`);
  }
}
