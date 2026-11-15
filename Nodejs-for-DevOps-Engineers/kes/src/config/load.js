// Layered configuration: defaults < project file < user file
// < profile < environment < flags (Chapter 7).
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { ConfigSchema } from './schema.js';
import { configDir } from '../lib/dirs.js';
import { CliError } from '../lib/errors.js';

export const DEFAULTS = {
  env: 'dev',
  region: 'eu-west-1',
  apiUrl: 'http://localhost:8080',
  timeoutMs: 5000,
  concurrency: 8,
  logLevel: 'info',
  catalogFile: 'services.yaml',
  registry: 'registry.example.com/kestrel',
};

const ENV_MAP = {
  KES_ENV: 'env',
  KES_REGION: 'region',
  KES_API_URL: 'apiUrl',
  KES_TIMEOUT_MS: 'timeoutMs',
  KES_CONCURRENCY: 'concurrency',
  KES_LOG_LEVEL: 'logLevel',
  KES_CATALOG: 'catalogFile',
  KES_SLACK_WEBHOOK: 'slackWebhook',
};

const FLAG_MAP = {
  env: 'env', region: 'region', timeout: 'timeoutMs',
  concurrency: 'concurrency',
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

function fromFlags(flags) {
  const out = {};
  for (const [flag, key] of Object.entries(FLAG_MAP)) {
    if (flags[flag] !== undefined) out[key] = flags[flag];
  }
  return out;
}

export async function loadConfig(flags = {}, opts = {}) {
  const env = opts.env ?? process.env;
  const cwd = opts.cwd ?? process.cwd();
  const userDir = opts.userDir ?? configDir;
  const project = await readOptionalJson(
    path.join(cwd, 'kes.config.json'));
  const user = await readOptionalJson(
    path.join(userDir, 'config.json'));
  const { profiles = {}, ...files } = { ...project, ...user };

  const profileName = flags.profile ?? env.KES_PROFILE;
  if (profileName && !profiles[profileName]) {
    const names = Object.keys(profiles).join(', ') || 'none';
    throw new CliError(`unknown profile ${profileName}; ` +
      `available: ${names}`, { code: 2 });
  }

  const merged = {
    ...DEFAULTS,
    ...files,
    ...(profiles[profileName] ?? {}),
    ...fromEnv(env),
    ...fromFlags(flags),
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

export function redact(config) {
  const copy = { ...config };
  for (const key of Object.keys(copy)) {
    if (/token|secret|password|webhook/i.test(key)) {
      copy[key] = copy[key] ? '***' : copy[key];
    }
  }
  return copy;
}
