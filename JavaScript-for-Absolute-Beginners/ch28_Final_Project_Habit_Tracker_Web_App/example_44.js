// Book: JavaScript for Absolute Beginners — Example 44
// js/storage.js
const KEY = "habitTracker.v1";

export function loadHabits() {
  try {
    const data = JSON.parse(localStorage.getItem(KEY));
    if (!Array.isArray(data)) return [];
    return data.filter(
      (h) => typeof h.id === "string"
        && typeof h.name === "string"
        && Array.isArray(h.done),
    );
  } catch {
    return [];
  }
}

export function saveHabits(habits) {
  try {
    localStorage.setItem(KEY, JSON.stringify(habits));
  } catch (error) {
    console.warn("Could not save habits:", error.message);
  }
}
