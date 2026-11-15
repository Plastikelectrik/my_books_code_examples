// Book: Node.js for DevOps Engineers — Example 192
// src/lib/logger.js
import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL ?? 'info',
  base: {
    service: process.env.SERVICE_NAME ?? 'kes',
    version: process.env.SERVICE_VERSION ?? 'dev',
    env: process.env.DEPLOY_ENV ?? 'local',
  },
  timestamp: pino.stdTimeFunctions.isoTime,
  formatters: {
    level: (label) => ({ level: label }),
  },
  redact: {
    paths: [
      'password', '*.password', 'token', '*.token',
      'authorization', 'req.headers.authorization',
      'req.headers.cookie', '*.secret', 'apiKey',
    ],
    censor: '[redacted]',
  },
});
