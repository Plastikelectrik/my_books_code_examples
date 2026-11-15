// Compare canary and baseline metrics (Chapter 13).
export const DEFAULT_RULES = [
  { metric: 'errorRate', max: 0.01 },
  { metric: 'p95Ms', maxRatio: 1.2, minSamples: 200 },
  { metric: 'p99Ms', maxRatio: 1.5, minSamples: 500 },
];

export function analyse(canary, baseline, rules) {
  const findings = [];
  for (const rule of rules ?? DEFAULT_RULES) {
    const c = canary[rule.metric];
    const b = baseline[rule.metric];
    const few = rule.minSamples
      && canary.requests < rule.minSamples;
    if (few) {
      findings.push({ ...rule, verdict: 'inconclusive',
        reason: `only ${canary.requests} requests` });
      continue;
    }
    if (rule.max !== undefined && c > rule.max) {
      findings.push({ ...rule, verdict: 'fail',
        reason: `${c} > ${rule.max}` });
    } else if (rule.maxRatio !== undefined
      && b > 0 && c / b > rule.maxRatio) {
      findings.push({ ...rule, verdict: 'fail',
        reason: `${(c / b).toFixed(2)}x baseline` });
    } else {
      findings.push({ ...rule, verdict: 'pass' });
    }
  }
  return findings;
}

export function decide(findings) {
  if (findings.some((f) => f.verdict === 'fail')) {
    return 'rollback';
  }
  if (findings.some((f) => f.verdict === 'inconclusive')) {
    return 'hold';
  }
  return 'promote';
}
