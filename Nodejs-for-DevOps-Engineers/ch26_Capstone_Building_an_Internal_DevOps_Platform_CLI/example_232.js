// Book: Node.js for DevOps Engineers — Example 232
// src/commands/delivery/index.js
export default {
  name: 'delivery',
  owner: 'platform',
  commands: {
    deploy: () => import('./deploy.js'),
    rollback: () => import('./rollback.js'),
    release: () => import('./release.js'),
  },
};
