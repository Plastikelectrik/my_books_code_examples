// Book: Node.js for DevOps Engineers — Example 86
// test/api-client.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  MockAgent, setGlobalDispatcher,
} from 'undici';
import { createClient } from '../src/lib/api-client.js';

test('retries a 503 then succeeds', async () => {
  const agent = new MockAgent();
  agent.disableNetConnect();
  setGlobalDispatcher(agent);
  const pool = agent.get('https://api.example.com');
  pool.intercept({ path: '/status' }).reply(503, '');
  pool.intercept({ path: '/status' })
    .reply(200, { ok: true });

  const api = createClient({
    baseUrl: 'https://api.example.com',
  });
  const { data } = await api.get('/status');
  assert.deepEqual(data, { ok: true });
});
