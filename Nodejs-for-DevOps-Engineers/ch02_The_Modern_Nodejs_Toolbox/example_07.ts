// Book: Node.js for DevOps Engineers — Example 07
// src/lib/service.ts
export interface Service {
  name: string;
  url: string;
  team: string;
  critical?: boolean;
}

export function label(s: Service): string {
  const flag = s.critical ? ' [critical]' : '';
  return `${s.name} (${s.team})${flag}`;
}
