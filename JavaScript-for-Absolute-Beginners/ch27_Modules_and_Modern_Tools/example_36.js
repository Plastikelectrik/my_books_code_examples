// Book: JavaScript for Absolute Beginners — Example 36
// storage.js
const PREFIX = "copperKettle.v1.";

export default {
  load(key, fallback) {
    try {
      const text = localStorage.getItem(PREFIX + key);
      return text === null ? fallback : JSON.parse(text);
    } catch {
      return fallback;
    }
  },
  save(key, value) {
    const text = JSON.stringify(value);
    localStorage.setItem(PREFIX + key, text);
  },
};
