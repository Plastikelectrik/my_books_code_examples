// Book: Node.js for DevOps Engineers — Example 195
// src/telemetry/instrumentation.js
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from
  '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from
  '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from
  '@opentelemetry/exporter-metrics-otlp-http';
import { PeriodicExportingMetricReader } from
  '@opentelemetry/sdk-metrics';

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter(),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter(),
    exportIntervalMillis: 15_000,
  }),
  instrumentations: [getNodeAutoInstrumentations({
    '@opentelemetry/instrumentation-fs': { enabled: false },
  })],
});

sdk.start();

process.once('SIGTERM', () => {
  sdk.shutdown().finally(() => process.exit(0));
});
