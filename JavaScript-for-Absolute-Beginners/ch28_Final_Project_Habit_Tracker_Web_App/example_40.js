// Book: JavaScript for Absolute Beginners — Example 40
// js/dates.js
export function dateKey(date = new Date()) {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, "0");
  const d = String(date.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

export function addDays(date, days) {
  const copy = new Date(date);
  copy.setDate(copy.getDate() + days);
  return copy;
}

export function lastDays(count, today = new Date()) {
  const days = [];
  for (let i = count - 1; i >= 0; i--) {
    days.push(addDays(today, -i));
  }
  return days;
}

export function shortDay(date) {
  return date.toLocaleDateString("en-GB", {
    weekday: "short",
  });
}
