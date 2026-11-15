// Book: JavaScript for Absolute Beginners — Example 30
// storage.js
const PREFIX = "copperKettle.v1.";

const storage = {
  load(key, fallback) {
    try {
      const text = localStorage.getItem(PREFIX + key);
      return text === null ? fallback : JSON.parse(text);
    } catch {
      return fallback;
    }
  },
  save(key, value) {
    try {
      const text = JSON.stringify(value);
      localStorage.setItem(PREFIX + key, text);
      return true;
    } catch {
      return false;
    }
  },
  remove(key) {
    localStorage.removeItem(PREFIX + key);
  },
};
