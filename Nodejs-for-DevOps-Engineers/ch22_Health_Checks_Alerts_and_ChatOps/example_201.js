// Book: Node.js for DevOps Engineers — Example 201
// src/alerts/model.js
/**
 * @typedef {object} Alert
 * @property {string} key      stable identity for dedup
 * @property {'critical'|'warning'|'info'} severity
 * @property {'firing'|'resolved'} status
 * @property {string} service
 * @property {string} title
 * @property {string} [detail]
 * @property {Record<string,string>} [labels]
 * @property {string} [runbook]
 * @property {string} startsAt ISO time
 */

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
