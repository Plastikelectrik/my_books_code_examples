// Book: Node.js for DevOps Engineers — Example 208
// src/chatops/commands.js
export const COMMANDS = {
  status: {
    risk: 'read',
    run: async ({ args, deps }) =>
      deps.formatStatus(await deps.status(args[0])),
  },
  logs: {
    risk: 'read',
    run: async ({ args, deps }) =>
      deps.formatErrors(
        await deps.topErrors(args[0], '15m')),
  },
  rollback: {
    risk: 'write',
    approvals: 1,
    run: async ({ args, deps, actor }) =>
      deps.rollback(args[0], { actor }),
  },
};

export function authorize(cmd, user, perms) {
  if (cmd.risk === 'read') return true;
  return perms.deployers.includes(user);
}
