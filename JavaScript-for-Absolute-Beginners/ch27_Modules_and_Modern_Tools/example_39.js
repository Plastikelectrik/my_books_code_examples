// Book: JavaScript for Absolute Beginners — Example 39
// js/basket.js
import storage from "./storage.js";

export function createBasket() {
  const lines = storage.load("basket", []);
  const save = () => storage.save("basket", lines);

  return {
    lines: () => lines.map((l) => ({ ...l })),
    add(item) {
      const name = item.name;
      const line = lines.find((l) => l.name === name);
      if (line) line.qty++;
      else lines.push({ ...item, qty: 1 });
      save();
    },
    clear() {
      lines.length = 0;
      save();
    },
  };
}
