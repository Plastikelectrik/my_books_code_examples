// Book: Node.js for DevOps Engineers — Example 220
// src/http/schemas.js
import { z } from 'zod';

export const CreateParcel = z.object({
  carrier: z.enum(['acme', 'swiftship', 'synthetic']),
  reference: z.string().min(1).max(64)
    .regex(/^[A-Za-z0-9_-]+$/),
  recipient: z.object({
    name: z.string().min(1).max(120),
    postcode: z.string().max(16),
  }),
  notify: z.array(z.enum(['sms', 'email'])).max(2)
    .default([]),
}).strict();
