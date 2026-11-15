// Book: Node.js for DevOps Engineers — Example 61
// src/lib/errors.js
export class CliError extends Error {
  constructor(message, { code = 1, cause } = {}) {
    super(message, { cause });
    this.name = 'CliError';
    this.exitCode = code;
  }
}

export function exitCodeFor(err) {
  if (err instanceof CliError) return err.exitCode;
  if (err.code?.startsWith?.('ERR_PARSE_ARGS')) return 2;
  if (err.name === 'TimeoutError') return 124;
  if (err.name === 'AbortError') return 130;
  return 1;
}
