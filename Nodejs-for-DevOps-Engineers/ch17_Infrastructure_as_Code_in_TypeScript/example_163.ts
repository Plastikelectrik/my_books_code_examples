// Book: Node.js for DevOps Engineers — Example 163
// infra/index.ts
import { ServiceQueue } from
  './components/service-queue.ts';

const services = [
  { service: 'tracking', team: 'core' },
  { service: 'notifications', team: 'comms' },
  { service: 'billing', team: 'payments', maxReceives: 3 },
];

export const queues = Object.fromEntries(
  services.map((s) => {
    const q = new ServiceQueue(`${s.service}-events`, {
      ...s, alarmTopicArn: alertsTopic.arn,
    });
    return [s.service, q.queueUrl];
  }),
);
