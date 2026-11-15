// Book: Node.js for DevOps Engineers — Example 164
// infra/config.ts
import * as pulumi from '@pulumi/pulumi';
import { z } from 'zod';

const Schema = z.object({
  env: z.enum(['staging', 'production']),
  dbInstanceClass: z.string().startsWith('db.'),
  minReplicas: z.coerce.number().int().min(1).max(20),
});

const cfg = new pulumi.Config();
export const settings = Schema.parse({
  env: pulumi.getStack(),
  dbInstanceClass: cfg.require('dbInstanceClass'),
  minReplicas: cfg.get('minReplicas') ?? '2',
});
