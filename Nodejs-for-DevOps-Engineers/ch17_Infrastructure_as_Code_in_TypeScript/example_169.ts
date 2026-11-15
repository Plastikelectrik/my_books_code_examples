// Book: Node.js for DevOps Engineers — Example 169
// src/infra/preview-env.ts
import { LocalWorkspace } from '@pulumi/pulumi/automation';

export async function upPreview(pr: number) {
  const stack = await LocalWorkspace.createOrSelectStack({
    stackName: `pr-${pr}`,
    workDir: 'infra/preview',
  });
  await stack.setConfig('aws:region',
    { value: 'eu-west-1' });
  await stack.setConfig('prNumber', { value: String(pr) });

  const result = await stack.up({
    onOutput: (line) => process.stderr.write(line),
  });
  return {
    url: result.outputs.url?.value as string,
    summary: result.summary.resourceChanges,
  };
}

export async function destroyPreview(pr: number) {
  const stack = await LocalWorkspace.selectStack({
    stackName: `pr-${pr}`, workDir: 'infra/preview',
  });
  await stack.destroy({ onOutput: () => {} });
  await stack.workspace.removeStack(`pr-${pr}`);
}
