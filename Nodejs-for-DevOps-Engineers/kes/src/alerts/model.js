// A common alert shape, from Prometheus-style input (Chapter 22).
export function fromPrometheus(a) {
  return {
    key: `${a.labels.alertname}:${a.labels.service}` +
      `:${a.labels.region ?? ''}`,
    severity: a.labels.severity ?? 'warning',
    status: a.status,
    service: a.labels.service ?? 'unknown',
    title: a.annotations?.summary ?? a.labels.alertname,
    detail: a.annotations?.description,
    labels: a.labels,
    runbook: a.annotations?.runbook_url,
    startsAt: a.startsAt,
  };
}

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
