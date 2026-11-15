// Book: Node.js for DevOps Engineers — Example 165
// cdk/lib/service-queue.ts
import { Construct } from 'constructs';
import { Duration, Tags } from 'aws-cdk-lib';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as cw from 'aws-cdk-lib/aws-cloudwatch';
import * as actions from
  'aws-cdk-lib/aws-cloudwatch-actions';
import * as sns from 'aws-cdk-lib/aws-sns';

export interface ServiceQueueProps {
  service: string;
  team: string;
  alarmTopic: sns.ITopic;
}

export class ServiceQueue extends Construct {
  readonly queue: sqs.Queue;

  constructor(scope: Construct, id: string,
    props: ServiceQueueProps) {
    super(scope, id);
    const dlq = new sqs.Queue(this, 'Dlq', {
      retentionPeriod: Duration.days(14),
    });
    this.queue = new sqs.Queue(this, 'Queue', {
      visibilityTimeout: Duration.seconds(60),
      deadLetterQueue: { queue: dlq, maxReceiveCount: 5 },
    });
    const alarm = dlq
      .metricApproximateNumberOfMessagesVisible()
      .createAlarm(this, 'DlqAlarm', {
        threshold: 0,
        evaluationPeriods: 1,
        comparisonOperator:
          cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
      });
    alarm.addAlarmAction(
      new actions.SnsAction(props.alarmTopic));
    Tags.of(this).add('service', props.service);
    Tags.of(this).add('team', props.team);
  }
}
