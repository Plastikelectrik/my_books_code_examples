// Book: Node.js for DevOps Engineers — Example 161
// infra/index.ts
import * as aws from '@pulumi/aws';
import * as pulumi from '@pulumi/pulumi';

const config = new pulumi.Config();
const env = pulumi.getStack(); // "staging", "production"

const photos = new aws.s3.Bucket('delivery-photos', {
  tags: { service: 'tracking', env },
});

new aws.s3.BucketPublicAccessBlock('photos-block', {
  bucket: photos.id,
  blockPublicAcls: true,
  blockPublicPolicy: true,
  ignorePublicAcls: true,
  restrictPublicBuckets: true,
});

new aws.s3.BucketLifecycleConfiguration('photos-life', {
  bucket: photos.id,
  rules: [{
    id: 'expire-old',
    status: 'Enabled',
    expiration: {
      days: config.getNumber('photoRetentionDays') ?? 365,
    },
  }],
});

export const bucketName = photos.bucket;
