// Bash-like brevity without shell injection (Chapter 5).
import { run } from './run.js';

export function $(strings, ...values) {
  const parts = [];
  strings.forEach((s, i) => {
    parts.push(...s.split(/\s+/).filter(Boolean));
    if (i < values.length) {
      const v = values[i];
      parts.push(...(Array.isArray(v) ? v : [String(v)]));
    }
  });
  const [cmd, ...args] = parts;
  return run(cmd, args);
}
