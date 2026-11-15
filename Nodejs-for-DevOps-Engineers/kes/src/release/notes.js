// Release notes in Markdown (Chapter 12).
const SECTIONS = [
  ['breaking', '⚠ Breaking changes'],
  ['feat', 'Features'],
  ['fix', 'Bug fixes'],
  ['perf', 'Performance'],
];

export function renderNotes(version, commits, opts) {
  const { repoUrl, date } = opts;
  const lines = [`## ${version} (${date})`, ''];
  for (const [key, title] of SECTIONS) {
    const items = commits.filter((c) =>
      key === 'breaking' ? c.breaking : c.type === key);
    if (!items.length) continue;
    lines.push(`### ${title}`, '');
    for (const c of items) {
      const scope = c.scope ? `**${c.scope}:** ` : '';
      const short = c.hash.slice(0, 7);
      lines.push(`- ${scope}${c.description} ` +
        `([${short}](${repoUrl}/commit/${c.hash}))`);
    }
    lines.push('');
  }
  return lines.join('\n');
}
