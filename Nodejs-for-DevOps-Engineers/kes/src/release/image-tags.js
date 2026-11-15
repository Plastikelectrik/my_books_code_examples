// Image tags for a release (Chapter 12).
export function imageTags(o) {
  const { registry, name, sha, version } = o;
  const base = `${registry}/${name}`;
  const tags = [`${base}:${sha}`];
  if (version) {
    const [major, minor] = version.split('.');
    tags.push(`${base}:${version}`,
      `${base}:${major}.${minor}`, `${base}:${major}`);
  }
  return tags;
}
