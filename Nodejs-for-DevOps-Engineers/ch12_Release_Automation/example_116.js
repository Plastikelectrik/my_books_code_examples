// Book: Node.js for DevOps Engineers — Example 116
// examples/semver-demo.js
import semver from 'semver';

console.log(semver.inc('1.4.2', 'minor'));     // 1.5.0
console.log(semver.inc('2.0.0-rc.1', 'prerelease'));
console.log(semver.satisfies('1.5.0', '^1.4.0'));
console.log(semver.gt('1.10.0', '1.9.0'));     // true
