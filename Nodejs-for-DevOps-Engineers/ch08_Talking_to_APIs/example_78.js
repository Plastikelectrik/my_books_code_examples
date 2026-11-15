// Book: Node.js for DevOps Engineers — Example 78
// src/lib/paginate.js (cursor style)
export async function* paginateCursor(client, path, opts) {
  const { itemsKey = 'items', cursorKey = 'next_cursor' } =
    opts ?? {};
  let cursor;
  do {
    const { data } = await client.get(path, {
      query: { cursor, limit: 100 },
    });
    yield* data[itemsKey];
    cursor = data[cursorKey];
  } while (cursor);
}
