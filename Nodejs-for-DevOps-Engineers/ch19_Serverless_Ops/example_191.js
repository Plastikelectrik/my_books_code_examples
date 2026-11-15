// Book: Node.js for DevOps Engineers — Example 191
// scripts/invoke-local.js
const [, , file, eventFile] = process.argv;
const { handler } = await import(file);
const { readFile } = await import('node:fs/promises');
const event = JSON.parse(await readFile(eventFile, 'utf8'));
console.log(await handler(event, {
  awsRequestId: 'local',
  getRemainingTimeInMillis: () => 60_000,
}));
