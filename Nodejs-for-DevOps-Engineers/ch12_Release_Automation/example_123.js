// Book: Node.js for DevOps Engineers — Example 123
// src/release/image-tags.js
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
