export const TEAS = {
  green: { temp: 80, base: 120 },
  black: { temp: 95, base: 240 },
  oolong: { temp: 90, base: 180 },
  herbal: { temp: 100, base: 300 },
};

export function brewTime(tea, strength) {
  const t = TEAS[tea];
  if (!t) return -1;
  let s = t.base + (strength - 3) * 20;
  if (t.temp < 85) s += (85 - t.temp) * 2;
  return Math.max(s, 30);
}
