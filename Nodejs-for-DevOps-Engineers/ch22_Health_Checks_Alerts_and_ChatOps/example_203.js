// Book: Node.js for DevOps Engineers — Example 203
// src/alerts/enrich.js
export async function enrich(alert, deps) {
  const [deploy, errors] = await Promise.allSettled([
    deps.lastDeploy(alert.service),
    deps.topErrors(alert.service, '15m'),
  ]);
  const extra = [];
  if (deploy.status === 'fulfilled' && deploy.value) {
    const d = deploy.value;
    const mins = Math.round((Date.now() - Date.parse(d.at))
      / 60_000);
    extra.push(`Last deploy: ${d.version} by ${d.actor}, ` +
      `${mins} min ago`);
  }
  if (errors.status === 'fulfilled') {
    for (const e of errors.value.slice(0, 3)) {
      extra.push(`• ${e.count}× ${e.msg}`);
    }
  }
  return { ...alert, context: extra };
}
