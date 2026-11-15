// Book: Node.js for DevOps Engineers — Example 66
// src/config/load.js
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { ConfigSchema } from './schema.js';
import { configDir } from '../lib/dirs.js';
import { CliError } from '../lib/errors.js';

const DEFAULTS = {
  env: 'dev',
  region: 'eu-west-1',
  apiUrl: 'http://localhost:8080',
  timeoutMs: 5000,
  concurrency: 8,
  logLevel: 'info',
};

const ENV_MAP = {
  KES_ENV: 'env',
  KES_REGION: 'region',
  KES_API_URL: 'apiUrl',
  KES_TIMEOUT_MS: 'timeoutMs',
  KES_CONCURRENCY: 'concurrency',
  KES_LOG_LEVEL: 'logLevel',
  KES_SLACK_WEBHOOK: 'slackWebhook',
};

async function readOptionalJson(file) {
  try {
    return JSON.parse(await readFile(file, 'utf8'));
  } catch (err) {
    if (err.code === 'ENOENT') return {};
    throw new CliError(`invalid config file ${file}`,
      { code: 2, cause: err });
  }
}

function fromEnv(env) {
  const out = {};
  for (const [name, key] of Object.entries(ENV_MAP)) {
    if (env[name] !== undefined && env[name] !== '') {
      out[key] = env[name];
    }
  }
  return out;
}

export async function loadConfig(flags = {}, opts = {}) {
  const env = opts.env ?? process.env;
  const cwd = opts.cwd ?? process.cwd();
  const merged = {
    ...DEFAULTS,
    ...(await readOptionalJson(
      path.join(cwd, 'kes.config.json'))),
    ...(await readOptionalJson(
      path.join(configDir, 'config.json'))),
    ...fromEnv(env),
    ...dropUndefined(flags),
  };

  const parsed = ConfigSchema.safeParse(merged);
  if (!parsed.success) {
    const lines = parsed.error.issues.map(
      (i) => `  ${i.path.join('.')}: ${i.message}`,
    );
    throw new CliError(
      `invalid configuration:\n${lines.join('\n')}`,
      { code: 2 },
    );
  }
  return Object.freeze(parsed.data);
}

function dropUndefined(obj) {
  return Object.fromEntries(
    Object.entries(obj).filter(([, v]) => v !== undefined),
  );
}
