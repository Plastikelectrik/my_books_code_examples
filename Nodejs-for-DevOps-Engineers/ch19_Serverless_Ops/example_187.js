// Book: Node.js for DevOps Engineers — Example 187
// functions/notify-worker/index.mjs
export const handler = async (event) => {
  const failures = [];
  await Promise.all(event.Records.map(async (record) => {
    try {
      const msg = JSON.parse(record.body);
      await sendNotification(msg);
    } catch (err) {
      console.error(JSON.stringify({
        msg: 'record failed',
        id: record.messageId,
        error: err.message,
      }));
      failures.push({ itemIdentifier: record.messageId });
    }
  }));
  return { batchItemFailures: failures };
};
