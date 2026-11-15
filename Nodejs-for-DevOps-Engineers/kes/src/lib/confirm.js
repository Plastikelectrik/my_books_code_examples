// Ask only when a human is present; require --yes otherwise (Chapter 6).
import { createInterface } from 'node:readline/promises';
import { CliError } from './errors.js';

export async function confirm(question, { yes }) {
  if (yes) return true;
  if (!process.stdin.isTTY) {
    throw new CliError(
      `${question} Refusing without --yes (not a terminal)`,
      { code: 2 },
    );
  }
  const rl = createInterface({
    input: process.stdin,
    output: process.stderr,
  });
  try {
    const answer = await rl.question(`${question} [y/N] `);
    return /^y(es)?$/i.test(answer.trim());
  } finally {
    rl.close();
  }
}
