// Book: JavaScript for Absolute Beginners — Example 21
// menu-model.js
const menu = [
  { name: "Latte", price: 3.9, category: "coffee",
    allergens: ["milk"] },
  { name: "Mocha", price: 4.3, category: "coffee",
    allergens: ["milk"] },
  { name: "Chai", price: 3.5, category: "tea",
    allergens: [] },
  { name: "Almond croissant", price: 3.2,
    category: "food", allergens: ["nuts", "gluten"] },
];

function describe({ name, price, allergens }) {
  const warn = allergens.length
    ? ` (contains ${allergens.join(", ")})`
    : "";
  return `${name}: ${price.toFixed(2)}${warn}`;
}

function findItem(name) {
  for (const item of menu) {
    if (item.name.toLowerCase() === name.toLowerCase()) {
      return item;
    }
  }
  return null;
}

function safeFor(allergen) {
  const safe = [];
  for (const item of menu) {
    if (!item.allergens.includes(allergen)) {
      safe.push(item.name);
    }
  }
  return safe;
}

console.log(describe(menu[3]));
console.log(findItem("CHAI")?.price);
console.log(findItem("tea") ?? "Not on the menu");
console.log(`Milk-free: ${safeFor("milk").join(", ")}`);
