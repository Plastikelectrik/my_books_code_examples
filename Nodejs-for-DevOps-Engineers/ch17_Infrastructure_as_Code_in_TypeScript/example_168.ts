// Book: Node.js for DevOps Engineers — Example 168
// cdk/lib/require-versioning.ts
import { IAspect, Annotations } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { IConstruct } from 'constructs';

type Versioning =
  s3.CfnBucket.VersioningConfigurationProperty;

export class RequireVersioning implements IAspect {
  visit(node: IConstruct) {
    if (!(node instanceof s3.CfnBucket)) return;
    const v = node.versioningConfiguration as
      Versioning | undefined;
    if (v?.status !== 'Enabled') {
      Annotations.of(node).addError(
        'S3 buckets must have versioning enabled');
    }
  }
}
