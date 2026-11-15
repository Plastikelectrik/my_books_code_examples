// Book: Node.js for DevOps Engineers — Example 206
// src/alerts/route.js
const ROUTES = {
  tracking: { channel: 'C-core-alerts', team: 'core' },
  billing: { channel: 'C-payments-alerts',
    team: 'payments' },
};
const FALLBACK = { channel: 'C-platform-alerts',
  team: 'platform' };

export function route(alert) {
  const r = ROUTES[alert.service] ?? FALLBACK;
  return {
    channel: r.channel,
    page: alert.severity === 'critical',
    team: r.team,
  };
}
