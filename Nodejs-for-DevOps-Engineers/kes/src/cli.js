#!/usr/bin/env node
// kes: Kestrel Logistics platform CLI (Chapters 6 and 26).
import { parseArgs, styleText } from 'node:util';
import { createContext } from './context.js';
import { CliError, exitCodeFor } from './lib/errors.js';
import { COMMANDS } from './commands/index.js';

const GLOBAL = {
  json: { type: 'boolean', default: false,
    description: 'Machine-readable JSON output' },
  verbose: { type: 'boolean', short: 'v', default: false,
    description: 'Show debug output' },
  help: { type: 'boolean', short: 'h', default: false,
    description: 'Show help' },
  profile: { type: 'string',
    description: 'Configuration profile' },
  env: { type: 'string', short: 'e',
    description: 'Environment (staging, production)' },
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

function printHelp(meta, options) {
  console.log(`${meta.summary}\n`);
  console.log(`Usage: ${meta.usage}\n`);
  console.log('Options:');
  for (const [name, o] of Object.entries(options)) {
    const short = o.short ? `-${o.short}, ` : '    ';
    const flag = `${short}--${name}`.padEnd(22);
    const hasDef = o.default !== undefined
      && o.type === 'string';
    const def = hasDef ? ` (default: ${o.default})` : '';
    console.log(`  ${flag}${o.description ?? ''}${def}`);
  }
}

function printRootHelp(unknown) {
  if (unknown && !unknown.startsWith('-')) {
    const msg = `unknown command: ${unknown}`;
    console.error(styleText('red', msg));
    process.exitCode = 2;
  }
  console.log('Usage: kes <command> [options]\n');
  console.log('Commands:');
  for (const name of Object.keys(COMMANDS)) {
    console.log(`  ${name}`);
  }
  console.log('\nRun "kes <command> --help" for details.');
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

  const ctx = await createContext(found.key, values);
  await mod.run(ctx, { values, positionals });
}

try {
  await main(process.argv.slice(2));
} catch (err) {
  console.error(`kes: ${err.message}`);
  if (process.env.KES_DEBUG) console.error(err);
  process.exitCode = exitCodeFor(err);
}

export { CliError };
