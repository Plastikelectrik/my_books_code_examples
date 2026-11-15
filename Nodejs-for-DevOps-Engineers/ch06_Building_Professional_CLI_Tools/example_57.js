// Book: Node.js for DevOps Engineers — Example 57
// src/commands/health.js
export const meta = {
  name: 'health',
  summary: 'Check health endpoints of all services',
  usage: 'kes health [--service NAME] [--json]',
  options: {
    service: { type: 'string', short: 's',
      description: 'Only check this service' },
    timeout: { type: 'string', default: '3000',
      description: 'Timeout per request in ms' },
  },
};

export async function run({ values, out }) {
  // implementation later in this chapter
}
