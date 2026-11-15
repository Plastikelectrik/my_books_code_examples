// Decide what a deploy will do; no side effects (Chapters 5, 26).
const ENVS = new Set(['staging', 'production']);

export function planDeploy({ svc, env, sha, registry }) {
  if (!svc) throw new Error('service is required');
  if (!ENVS.has(env)) {
    throw new Error(`unknown environment: ${env}`);
  }
  if (!/^[0-9a-f]{7,40}$/.test(sha)) {
    throw new Error(`invalid git sha: ${sha}`);
  }
  if (svc.runtime.kind !== 'kubernetes') {
    throw new Error(`${svc.name}: only kubernetes ` +
      'services can be deployed by kes deploy');
  }
  const image = `${registry}/${svc.name}:${sha}`;
  const { namespace, deployment, container } = svc.runtime;
  const kube = ['--context', env, '-n', namespace];
  return {
    service: svc.name,
    env,
    image,
    strategy: svc.deploy.strategy,
    steps: [
      ['docker', ['build', '-t', image,
        `services/${svc.name}`]],
      ['docker', ['push', image]],
      ['kubectl', [...kube, 'set', 'image',
        `deploy/${deployment}`, `${container}=${image}`]],
      ['kubectl', [...kube, 'rollout', 'status',
        `deploy/${deployment}`, '--timeout=300s']],
    ],
  };
}
