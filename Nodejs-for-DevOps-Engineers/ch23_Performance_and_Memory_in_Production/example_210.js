// Book: Node.js for DevOps Engineers — Example 210
// src/telemetry/loop-delay.js
import { monitorEventLoopDelay } from 'node:perf_hooks';
import { metrics } from '@opentelemetry/api';

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

const meter = metrics.getMeter('kestrel.runtime');
meter.createObservableGauge('nodejs.eventloop.delay.p99', {
  unit: 's',
  description: 'p99 event loop delay since last export',
}).addCallback((r) => {
  r.observe(h.percentile(99) / 1e9);
  h.reset();
});
