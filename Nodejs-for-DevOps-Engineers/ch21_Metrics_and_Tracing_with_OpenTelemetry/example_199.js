// Book: Node.js for DevOps Engineers — Example 199
// src/telemetry/cli-tracing.js
import { trace, context, propagation } from
  '@opentelemetry/api';

export async function startCliTracing() {
  if (!process.env.OTEL_EXPORTER_OTLP_ENDPOINT) return null;
  const { NodeSDK } = await import(
    '@opentelemetry/sdk-node');
  const { OTLPTraceExporter } = await import(
    '@opentelemetry/exporter-trace-otlp-http');
  const sdk = new NodeSDK({
    serviceName: 'kes',
    traceExporter: new OTLPTraceExporter(),
    instrumentations: [],
  });
  sdk.start();
  return sdk;
}

export async function traced(name, attrs, fn) {
  const tracer = trace.getTracer('kes');
  const parent = propagation.extract(context.active(), {
    traceparent: process.env.TRACEPARENT,
  });
  return context.with(parent, () =>
    tracer.startActiveSpan(name, async (span) => {
      span.setAttributes(attrs);
      try {
        return await fn(span);
      } catch (err) {
        span.recordException(err);
        span.setStatus({ code: 2 });
        throw err;
      } finally {
        span.end();
      }
    }));
}
