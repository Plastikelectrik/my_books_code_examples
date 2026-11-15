// Book: Node.js for DevOps Engineers — Example 110
// scripts/ci/context.js
import { readFile } from 'node:fs/promises';

export async function ciContext() {
  const env = process.env;
  const event = env.GITHUB_EVENT_PATH
    ? JSON.parse(
      await readFile(env.GITHUB_EVENT_PATH, 'utf8'))
    : {};
  return {
    repo: env.GITHUB_REPOSITORY,
    sha: env.GITHUB_SHA,
    ref: env.GITHUB_REF_NAME,
    eventName: env.GITHUB_EVENT_NAME,
    prNumber: event.pull_request?.number,
    actor: env.GITHUB_ACTOR,
    event,
  };
}
