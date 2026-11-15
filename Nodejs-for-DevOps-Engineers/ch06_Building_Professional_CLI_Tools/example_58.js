// Book: Node.js for DevOps Engineers — Example 58
// src/cli.js
import { parseArgs } from 'node:util';
import { createOutput } from './lib/output.js';
import { CliError, exitCodeFor } from './lib/errors.js';

const COMMANDS = {
  version: () => import('./commands/version.js'),
  health: () => import('./commands/health.js'),
  'certs check': () => import('./commands/certs/check.js'),
  deploy: () => import('./commands/deploy.js'),
};

const GLOBAL = {
  json: { type: 'boolean', default: false,
    description: 'Machine-readable JSON output' },
  verbose: { type: 'boolean', short: 'v', default: false,
    description: 'Show debug output' },
  help: { type: 'boolean', short: 'h', default: false,
    description: 'Show help' },
};

function findCommand(argv) {
  for (const len of [2, 1]) {
    const key = argv.slice(0, len).join(' ');
    if (COMMANDS[key]) {
      return { key, rest: argv.slice(len) };
    }
  }
  return null;
}

async function main(argv) {
  const found = findCommand(argv);
  if (!found) return printRootHelp(argv[0]);

  const mod = await COMMANDS[found.key]();
  const options = { ...GLOBAL, ...mod.meta.options };
  const { values, positionals } = parseArgs({
    args: found.rest, options, allowPositionals: true,
  });
  if (values.help) return printHelp(mod.meta, options);

  const out = createOutput(values);
  await mod.run({ values, positionals, out });
}

try {
  await main(process.argv.slice(2));
} catch (err) {
  console.error(`kes: ${err.message}`);
  if (process.env.KES_DEBUG) console.error(err);
  process.exitCode = exitCodeFor(err);
}
