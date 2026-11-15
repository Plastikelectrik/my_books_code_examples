// Book: Node.js for DevOps Engineers — Example 52
// src/deploy/plan.js
const ENVS = new Set(['staging', 'production']);
const REGISTRY = 'registry.example.com/kestrel';

export function planDeploy({ service, env, sha }) {
  if (!service) throw new Error('service is required');
  if (!ENVS.has(env)) {
    throw new Error(`unknown environment: ${env}`);
  }
  const image = `${REGISTRY}/${service}:${sha}`;
  const kube = ['--context', env, '-n', service];
  return {
    image,
    steps: [
      ['docker', ['build', '-t', image,
        `services/${service}`]],
      ['docker', ['push', image]],
      ['kubectl', [...kube, 'set', 'image',
        `deploy/${service}`, `app=${image}`]],
      ['kubectl', [...kube, 'rollout', 'status',
        `deploy/${service}`, '--timeout=300s']],
    ],
  };
}
