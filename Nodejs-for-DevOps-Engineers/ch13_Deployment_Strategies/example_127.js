// Book: Node.js for DevOps Engineers — Example 127
// src/canary/metrics.js
import { createClient } from '../lib/api-client.js';

export function prometheus(baseUrl) {
  const api = createClient({ baseUrl });

  async function scalar(query) {
    const { data } = await api.get('/api/v1/query',
      { query: { query } });
    const v = data.data.result[0]?.value?.[1];
    return v === undefined ? 0 : Number(v);
  }

  return async function snapshot(service, version, win) {
    const sel = `service="${service}",version="${version}"`;
    const total = `http_requests_total{${sel}}`;
    const failed =
      `http_requests_total{${sel},code=~"5.."}`;
    const buckets =
      `http_request_duration_seconds_bucket{${sel}}`;
    const reqs = `sum(increase(${total}[${win}]))`;
    const errs = `sum(increase(${failed}[${win}]))`;
    const p = (q) => `histogram_quantile(${q}, ` +
      `sum by (le) (rate(${buckets}[${win}])))`;

    const [requests, errors, p95, p99] = await Promise.all([
      scalar(reqs), scalar(errs), scalar(p(0.95)),
      scalar(p(0.99)),
    ]);
    return {
      requests,
      errorRate: requests ? errors / requests : 0,
      p95Ms: p95 * 1000,
      p99Ms: p99 * 1000,
    };
  };
}
