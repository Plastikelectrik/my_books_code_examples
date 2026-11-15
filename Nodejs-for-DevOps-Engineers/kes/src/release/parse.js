// Conventional Commits -> next version bump (Chapter 12).
const HEADER = /^(\w+)(?:\(([^)]+)\))?(!)?: (.+)$/;

export function parseCommit({ hash, subject, body = '' }) {
  const m = subject.match(HEADER);
  if (!m) return { hash, type: 'other', subject };
  const [, type, scope, bang, description] = m;
  const breaking = Boolean(bang)
    || /^BREAKING[ -]CHANGE:/m.test(body);
  return { hash, type, scope, description, breaking };
}

export function nextBump(commits) {
  if (commits.some((c) => c.breaking)) return 'major';
  if (commits.some((c) => c.type === 'feat')) {
    return 'minor';
  }
  if (commits.some((c) => c.type === 'fix'
    || c.type === 'perf')) return 'patch';
  return null;
}
