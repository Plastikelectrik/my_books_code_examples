// Book: Node.js for DevOps Engineers — Example 214
// src/lib/lru.js
export function lru(max, ttlMs) {
  const map = new Map();
  return {
    get(k) {
      const e = map.get(k);
      if (!e) return undefined;
      if (Date.now() > e.exp) {
        map.delete(k);
        return undefined;
      }
      map.delete(k);
      map.set(k, e); // move to newest
      return e.v;
    },
    set(k, v) {
      map.delete(k);
      map.set(k, { v, exp: Date.now() + ttlMs });
      if (map.size > max) {
        map.delete(map.keys().next().value);
      }
    },
  };
}
