// Book: Node.js for DevOps Engineers — Example 186
// functions/lib/idempotency.js
import {
  DynamoDBClient, PutItemCommand,
} from '@aws-sdk/client-dynamodb';

const db = new DynamoDBClient({});
const TABLE = process.env.IDEMPOTENCY_TABLE;

export async function once(key, fn) {
  const ttl = Math.floor(Date.now() / 1000) + 7 * 86_400;
  try {
    await db.send(new PutItemCommand({
      TableName: TABLE,
      Item: { pk: { S: key }, ttl: { N: String(ttl) } },
      ConditionExpression: 'attribute_not_exists(pk)',
    }));
  } catch (err) {
    if (err.name === 'ConditionalCheckFailedException') {
      return { skipped: true };
    }
    throw err;
  }
  return { skipped: false, result: await fn() };
}
