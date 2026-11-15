// Whole days between two dates (Chapter 2).
const DAY = 86_400_000;

export function daysUntil(date, now = new Date()) {
  return Math.floor((date - now) / DAY);
}
