// Book: Node.js for DevOps Engineers — Example 79
// src/integrations/github.js
import { createClient } from '../lib/api-client.js';

export function github(token) {
  return createClient({
    baseUrl: 'https://api.github.com',
    headers: {
      Authorization: `Bearer ${token.reveal()}`,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
    },
  });
}
