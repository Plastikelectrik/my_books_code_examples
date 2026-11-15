// Book: Node.js for DevOps Engineers — Example 227
// src/catalog/schema.js
import { z } from 'zod';

const Name = z.string().regex(/^[a-z][a-z0-9-]{1,40}$/);

export const ServiceSchema = z.object({
  name: Name,
  description: z.string().max(200),
  owner: z.object({
    team: Name,
    chat: z.string(),
    oncall: z.string().optional(),
  }),
  tier: z.union([z.literal(1), z.literal(2),
    z.literal(3)]),
  runtime: z.discriminatedUnion('kind', [
    z.object({ kind: z.literal('kubernetes'),
      namespace: Name, deployment: Name,
      container: Name }),
    z.object({ kind: z.literal('function'),
      functionName: z.string() }),
  ]),
  health: z.object({ url: z.url() }).optional(),
  deploy: z.object({
    strategy: z.enum(['rolling', 'canary']),
    steps: z.array(z.number().int().min(1).max(100))
      .optional(),
    bakeMinutes: z.number().int().min(1).max(60)
      .optional(),
  }),
  slo: z.object({
    availability: z.number().min(90).max(100),
    latencyP95Ms: z.number().int().positive(),
  }).optional(),
  dependencies: z.array(z.string()).default([]),
  links: z.record(z.string(), z.url()).default({}),
}).strict();
