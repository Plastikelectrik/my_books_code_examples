// Book: Node.js for DevOps Engineers — Example 213
// examples/redos.js
const bad = /^(\w+\s?)*$/;
const input = 'a'.repeat(30) + '!';
console.time('match');
bad.test(input);       // can take a very long time
console.timeEnd('match');
