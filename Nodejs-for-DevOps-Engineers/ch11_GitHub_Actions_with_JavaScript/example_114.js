// Book: Node.js for DevOps Engineers — Example 114
// actions/deploy-preview/src/index.js
import * as core from '@actions/core';
import * as github from '@actions/github';

const MARKER = '<!-- kes-deploy-preview -->';

try {
  const service = core.getInput('service',
    { required: true });
  const token = core.getInput('token');
  const { context } = github;
  const pr = context.payload.pull_request;
  if (!pr) {
    core.info('not a pull request, skipping');
  } else {
    const sha = pr.head.sha.slice(0, 7);
    const image = `registry.example.com/kestrel/` +
      `${service}:${sha}`;
    core.setOutput('image', image);

    const body = [
      MARKER,
      `### Deploy preview for \`${service}\``,
      `Image: \`${image}\``,
      '',
      '| Environment | When |',
      '| --- | --- |',
      '| staging | on merge to main |',
      '| production | after manual approval |',
    ].join('\n');

    await upsertComment(github.getOctokit(token),
      context, pr.number, body);
  }
} catch (err) {
  core.setFailed(err.message);
}
