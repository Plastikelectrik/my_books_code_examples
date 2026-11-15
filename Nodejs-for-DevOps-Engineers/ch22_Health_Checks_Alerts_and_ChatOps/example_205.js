// Book: Node.js for DevOps Engineers — Example 205
// src/alerts/format.js
const ICON = { critical: '🔴', warning: '🟠', info: '🔵' };

export function formatAlert(a, opts = {}) {
  const head = a.status === 'resolved'
    ? `✅ RESOLVED: ${a.title}`
    : `${ICON[a.severity]} ${a.severity.toUpperCase()}: ` +
      a.title;
  const lines = [
    `*${head}*`,
    `Service: \`${a.service}\``,
    a.detail ?? '',
    ...(a.context ?? []),
  ];
  if (opts.count > 1) {
    lines.push(`_Fired ${opts.count} times_`);
  }
  if (a.runbook) lines.push(`<${a.runbook}|Runbook>`);
  return lines.filter(Boolean).join('\n');
}
