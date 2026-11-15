// Book: Node.js for DevOps Engineers — Example 196
// src/tracking/eta.js
import { trace, SpanStatusCode } from '@opentelemetry/api';

const tracer = trace.getTracer('kestrel.tracking');

export async function estimateEta(parcel) {
  return tracer.startActiveSpan('eta.estimate',
    async (span) => {
    span.setAttributes({
      'parcel.carrier': parcel.carrier,
      'parcel.hops': parcel.hops.length,
    });
    try {
      const route = await loadRoute(parcel);
      const eta = computeEta(route);
      span.setAttribute('eta.hours', eta.hours);
      return eta;
    } catch (err) {
      span.recordException(err);
      span.setStatus({ code: SpanStatusCode.ERROR,
        message: err.message });
      throw err;
    } finally {
      span.end();
    }
  });
}
