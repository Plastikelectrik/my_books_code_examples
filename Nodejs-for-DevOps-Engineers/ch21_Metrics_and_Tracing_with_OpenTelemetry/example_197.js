// Book: Node.js for DevOps Engineers — Example 197
// src/telemetry/metrics.js
import { metrics } from '@opentelemetry/api';

const meter = metrics.getMeter('kestrel.notifications');

export const sent = meter.createCounter(
  'notifications.sent', {
    description: 'Notifications delivered',
    unit: '{notification}',
  });

export const latency = meter.createHistogram(
  'notifications.provider.duration', {
    description: 'Time spent calling the provider',
    unit: 's',
  });

export function trackQueue(getDepth) {
  meter.createObservableGauge('notifications.queue.depth', {
    description: 'Messages waiting',
  }).addCallback((result) => result.observe(getDepth()));
}
