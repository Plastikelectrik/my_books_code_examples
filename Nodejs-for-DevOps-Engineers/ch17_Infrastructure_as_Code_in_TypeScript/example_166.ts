// Book: Node.js for DevOps Engineers — Example 166
// infra/test/service-queue.test.ts
import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import * as pulumi from '@pulumi/pulumi';

before(() => {
  pulumi.runtime.setMocks({
    newResource: (args) => ({
      id: `${args.name}-id`,
      state: { ...args.inputs, arn: `arn:mock:${args.name}`,
        name: args.name },
    }),
    call: (args) => args.inputs,
  });
});

test('component exposes the queue ARN', async () => {
  const { ServiceQueue } = await import(
    '../components/service-queue.ts');
  const q = new ServiceQueue('t', {
    service: 'tracking', team: 'core',
    alarmTopicArn: 'arn:mock:topic',
  });
  const arn = await new Promise((resolve) =>
    q.queueArn.apply(resolve));
  assert.match(String(arn), /^arn:mock:t$/);
});
