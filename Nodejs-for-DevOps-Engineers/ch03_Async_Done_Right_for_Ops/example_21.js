// Book: Node.js for DevOps Engineers — Example 21
// examples/cancellable.js
import { withTimeout } from '../src/lib/cancel.js';

try {
  const res = await fetch('https://api.example.com/slow', {
    signal: withTimeout(10_000),
  });
  console.log(res.status);
} catch (err) {
  if (err.name === 'AbortError') {
    console.error('cancelled by user');
    process.exitCode = 130;
  } else if (err.name === 'TimeoutError') {
    console.error('timed out');
    process.exitCode = 124;
  } else {
    throw err;
  }
}
