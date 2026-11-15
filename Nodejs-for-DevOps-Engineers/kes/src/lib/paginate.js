// Async generators that hide pagination (Chapter 8).
export async function* paginateLinks(client, path, query) {
  const next = new URL(path, 'http://x');
  for (const [k, v] of Object.entries(query ?? {})) {
    next.searchParams.set(k, v);
  }
  let url = next.pathname + next.search;

  while (url) {
    const { data, headers } = await client.get(url);
    yield* data;
    url = parseNextLink(headers.get('link'));
  }
}

export function parseNextLink(header) {
  if (!header) return null;
  for (const part of header.split(',')) {
    const m = part.match(/<([^>]+)>;\s*rel="next"/);
    if (m) {
      const u = new URL(m[1]);
      return u.pathname + u.search;
    }
  }
  return null;
}
