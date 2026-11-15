// Book: Node.js for DevOps Engineers — Example 171
// examples/aws-whoami.js
import {
  STSClient, GetCallerIdentityCommand,
} from '@aws-sdk/client-sts';

const sts = new STSClient({});
const me = await sts.send(new GetCallerIdentityCommand({}));
console.log(`account ${me.Account}`);
console.log(`identity ${me.Arn}`);
