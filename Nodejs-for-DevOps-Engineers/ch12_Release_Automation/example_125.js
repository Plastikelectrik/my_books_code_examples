// Book: Node.js for DevOps Engineers — Example 125
// src/release/github-release.js
import { createClient } from '../lib/api-client.js';

export async function createGithubRelease(o) {
  const { repo, version, notes, token } = o;
  const gh = createClient({
    baseUrl: 'https://api.github.com',
    headers: { Authorization: `Bearer ${token}` },
  });
  const path = `/repos/${repo}/releases`;
  const { data } = await gh.post(path, {
    tag_name: `v${version}`,
    name: `v${version}`,
    body: notes,
    prerelease: version.includes('-'),
  });
  return data.html_url;
}
