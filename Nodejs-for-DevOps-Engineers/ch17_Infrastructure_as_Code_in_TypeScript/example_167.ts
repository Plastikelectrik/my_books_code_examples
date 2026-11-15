// Book: Node.js for DevOps Engineers — Example 167
// cdk/test/service-queue.test.ts
import { test } from 'node:test';
import { App, Stack } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import * as sns from 'aws-cdk-lib/aws-sns';
import { ServiceQueue } from '../lib/service-queue.ts';

test('creates a DLQ alarm', () => {
  const stack = new Stack(new App(), 'Test');
  const topic = new sns.Topic(stack, 'Alerts');
  new ServiceQueue(stack, 'Q', {
    service: 'tracking', team: 'core', alarmTopic: topic,
  });
  const t = Template.fromStack(stack);
  t.resourceCountIs('AWS::SQS::Queue', 2);
  t.hasResourceProperties('AWS::CloudWatch::Alarm', {
    Threshold: 0,
  });
});
