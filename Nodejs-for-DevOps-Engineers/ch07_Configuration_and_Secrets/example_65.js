// Book: Node.js for DevOps Engineers — Example 65
// src/config/schema.js
import { z } from 'zod';

export const ConfigSchema = z.object({
  env: z.enum(['dev', 'staging', 'production']),
  region: z.string().regex(/^[a-z]{2}-[a-z]+-\d$/),
  apiUrl: z.url(),
  timeoutMs: z.coerce.number().int()
    .min(100).max(120_000),
  concurrency: z.coerce.number().int().min(1).max(64),
  logLevel: z.enum(['debug', 'info', 'warn', 'error']),
  slackWebhook: z.url().optional(),
});
