// js/habits.js
import { dateKey, addDays } from "./dates.js";

export function createHabit(name, emoji = "✅") {
  return {
    id: `h${Date.now()}`,
    name: name.trim(),
    emoji,
    done: [],
  };
}

export function isDone(habit, key) {
  return habit.done.includes(key);
}

export function toggleDay(habit, key) {
  const done = isDone(habit, key)
    ? habit.done.filter((k) => k !== key)
    : [...habit.done, key].sort();
  return { ...habit, done };
}

export function streak(habit, today = new Date()) {
  let day = today;
  if (!isDone(habit, dateKey(day))) {
    // today not done yet: count from yesterday
    day = addDays(day, -1);
  }
  let count = 0;
  while (isDone(habit, dateKey(day))) {
    count++;
    day = addDays(day, -1);
  }
  return count;
}

export function validateName(name, habits) {
  const clean = name.trim();
  if (clean.length < 2) {
    return "Give the habit a name (at least 2 letters).";
  }
  if (clean.length > 40) {
    return "Keep the name under 40 characters.";
  }
  const exists = habits.some(
    (h) => h.name.toLowerCase() === clean.toLowerCase(),
  );
  if (exists) {
    return "You already track a habit with that name.";
  }
  return null;
}
