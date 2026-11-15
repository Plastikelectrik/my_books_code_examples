// Book: Node.js for DevOps Engineers — Example 10
// src/lib/days.js
const DAY = 86_400_000;

export function daysUntil(date, now = new Date()) {
  return Math.floor((date - now) / DAY);
}
