// Book: Node.js for DevOps Engineers — Example 46
// src/lib/stdin.js
import { text } from 'node:stream/consumers';

export async function readStdin() {
  if (process.stdin.isTTY) return '';
  return text(process.stdin);
}
