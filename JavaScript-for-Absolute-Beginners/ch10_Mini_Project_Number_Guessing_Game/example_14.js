// Book: JavaScript for Absolute Beginners — Example 14
// guess.mjs (step 1)
const MIN = 1;
const MAX = 50;
const secret =
  Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;

console.log(`(debug) secret is ${secret}`);
