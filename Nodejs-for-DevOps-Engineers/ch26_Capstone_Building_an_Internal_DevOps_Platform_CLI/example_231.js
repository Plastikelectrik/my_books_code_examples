// Book: Node.js for DevOps Engineers — Example 231
// src/commands/index.js
import core from './core/index.js';
import services from './services/index.js';
import delivery from './delivery/index.js';
import kube from './kube/index.js';
import cloud from './cloud/index.js';
import fleet from './fleet/index.js';

export const GROUPS = [core, services, delivery, kube,
  cloud, fleet];

export const COMMANDS = Object.fromEntries(
  GROUPS.flatMap((g) => Object.entries(g.commands)));
