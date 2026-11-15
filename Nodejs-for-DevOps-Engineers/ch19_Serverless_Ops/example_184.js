// Book: Node.js for DevOps Engineers — Example 184
// functions/weekly-costs/index.mjs
import { costByTag } from './lib/costs.js';
import { postToChat } from './lib/chat.js';

const WEBHOOK = process.env.CHAT_WEBHOOK_SECRET_ARN;

export const handler = async () => {
  const end = new Date();
  const start = new Date(end - 7 * 86_400_000);
  const iso = (d) => d.toISOString().slice(0, 10);

  const rows = await costByTag('service',
    iso(start), iso(end));
  const total = rows.reduce((s, [, v]) => s + v, 0);
  const lines = rows.slice(0, 8).map(([k, v]) =>
    `• ${k}: $${v.toFixed(0)}`);

  await postToChat(WEBHOOK, [
    `*Cloud cost, last 7 days: $${total.toFixed(0)}*`,
    ...lines,
  ].join('\n'));
  return { total };
};
