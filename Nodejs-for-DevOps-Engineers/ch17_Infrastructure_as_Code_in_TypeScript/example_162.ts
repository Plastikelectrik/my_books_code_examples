// Book: Node.js for DevOps Engineers — Example 162
// infra/components/service-queue.ts
import * as aws from '@pulumi/aws';
import * as pulumi from '@pulumi/pulumi';

export interface ServiceQueueArgs {
  service: string;
  team: string;
  maxReceives?: number;
  alarmTopicArn: pulumi.Input<string>;
}

export class ServiceQueue extends pulumi.ComponentResource {
  public readonly queueUrl: pulumi.Output<string>;
  public readonly queueArn: pulumi.Output<string>;

  constructor(name: string, args: ServiceQueueArgs,
    opts?: pulumi.ComponentResourceOptions) {
    super('kestrel:index:ServiceQueue', name, {}, opts);
    const tags = { service: args.service, team: args.team };
    const child = { parent: this };

    const dlq = new aws.sqs.Queue(`${name}-dlq`, {
      messageRetentionSeconds: 14 * 24 * 3600,
      tags,
    }, child);

    const queue = new aws.sqs.Queue(name, {
      visibilityTimeoutSeconds: 60,
      redrivePolicy: dlq.arn.apply((arn) => JSON.stringify({
        deadLetterTargetArn: arn,
        maxReceiveCount: args.maxReceives ?? 5,
      })),
      tags,
    }, child);

    new aws.cloudwatch.MetricAlarm(`${name}-dlq-alarm`, {
      namespace: 'AWS/SQS',
      metricName: 'ApproximateNumberOfMessagesVisible',
      dimensions: { QueueName: dlq.name },
      statistic: 'Maximum',
      period: 300,
      evaluationPeriods: 1,
      threshold: 0,
      comparisonOperator: 'GreaterThanThreshold',
      alarmActions: [args.alarmTopicArn],
      tags,
    }, child);

    this.queueUrl = queue.url;
    this.queueArn = queue.arn;
    this.registerOutputs({ queueUrl: this.queueUrl });
  }
}
