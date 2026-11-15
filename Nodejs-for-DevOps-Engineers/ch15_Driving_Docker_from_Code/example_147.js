// Book: Node.js for DevOps Engineers — Example 147
// src/docker/stats.js
export function cpuPercent(s) {
  const cpuDelta = s.cpu_stats.cpu_usage.total_usage
    - s.precpu_stats.cpu_usage.total_usage;
  const sysDelta = s.cpu_stats.system_cpu_usage
    - s.precpu_stats.system_cpu_usage;
  const cpus = s.cpu_stats.online_cpus ?? 1;
  if (sysDelta <= 0 || cpuDelta < 0) return 0;
  return (cpuDelta / sysDelta) * cpus * 100;
}

export function memoryUsage(s) {
  const cache = s.memory_stats.stats?.inactive_file ?? 0;
  const used = s.memory_stats.usage - cache;
  return {
    usedMb: used / 1048576,
    limitMb: s.memory_stats.limit / 1048576,
    percent: (used / s.memory_stats.limit) * 100,
  };
}
