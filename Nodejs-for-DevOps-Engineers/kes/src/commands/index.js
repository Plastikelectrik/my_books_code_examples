// Command table: each command is loaded only when used.
export const COMMANDS = {
  version: () => import('./core/version.js'),
  'config show': () => import('./core/config-show.js'),
  completion: () => import('./core/completion.js'),
  'services list': () => import('./services/list.js'),
  health: () => import('./services/health.js'),
  'certs check': () => import('./services/certs.js'),
  deploy: () => import('./delivery/deploy.js'),
  release: () => import('./delivery/release.js'),
  'canary demo': () => import('./delivery/canary-demo.js'),
  'kube audit': () => import('./kube/audit.js'),
  'fleet exec': () => import('./fleet/exec.js'),
  'fleet disk': () => import('./fleet/disk.js'),
  'docker cleanup': () => import('./docker/cleanup.js'),
  'supply audit': () => import('./supply/audit.js'),
};
