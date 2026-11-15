// Book: Node.js for DevOps Engineers — Example 204
// src/chat/client.js
import { createClient } from '../lib/api-client.js';

export function chatClient(token, baseUrl) {
  const api = createClient({
    baseUrl,
    headers: { Authorization: `Bearer ${token.reveal()}` },
  });
  return {
    async post(channel, blocks, text) {
      const { data } = await api.post('/chat.postMessage',
        { channel, text, blocks });
      return { channel, ts: data.ts };
    },
    async update(ref, blocks, text) {
      await api.post('/chat.update',
        { channel: ref.channel, ts: ref.ts, text, blocks });
    },
    async reply(ref, text) {
      await api.post('/chat.postMessage',
        { channel: ref.channel, thread_ts: ref.ts, text });
    },
  };
}
