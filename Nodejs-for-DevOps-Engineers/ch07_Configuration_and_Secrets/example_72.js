// Book: Node.js for DevOps Engineers — Example 72
// src/lib/ci.js
export function maskInCi(value) {
  if (process.env.GITHUB_ACTIONS === 'true' && value) {
    console.log(`::add-mask::${value}`);
  }
}
