// Read everything piped into the program (Chapter 4).
import { text } from 'node:stream/consumers';

export async function readStdin() {
  if (process.stdin.isTTY) return '';
  return text(process.stdin);
}
