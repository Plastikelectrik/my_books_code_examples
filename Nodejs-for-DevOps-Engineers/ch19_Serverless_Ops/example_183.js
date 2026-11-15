// Book: Node.js for DevOps Engineers — Example 183
// functions/hello/index.mjs
export const handler = async (event, context) => {
  console.log(JSON.stringify({
    msg: 'invoked',
    requestId: context.awsRequestId,
    source: event.source,
  }));
  return { ok: true };
};
