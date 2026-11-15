// Book: JavaScript for Absolute Beginners — Example 11
// order-advisor.js
const drink = " Mocha ";
const size = "large";
const isMember = true;
const note = "Allergic to NUTS";
const hour = 15;

const cleanDrink = drink.trim().toLowerCase();

let basePrice;
switch (size) {
  case "small":
    basePrice = 2.8;
    break;
  case "medium":
    basePrice = 3.4;
    break;
  case "large":
    basePrice = 3.9;
    break;
  default:
    basePrice = 3.4;
}

// Mochas cost a little more
if (cleanDrink === "mocha") {
  basePrice += 0.4;
}

let discount = 0;
if (isMember) {
  discount = 0.1;
} else if (hour >= 15 && hour < 17) {
  discount = 0.05; // happy hour for everyone else
}

const price = basePrice * (1 - discount);

console.log(`${size} ${cleanDrink}: ${price.toFixed(2)}`);

if (discount > 0) {
  const percent = discount * 100;
  console.log(`Includes a ${percent}% discount.`);
}

if (note.toLowerCase().includes("nut")) {
  console.log("WARNING: nut allergy, tell the kitchen!");
}

const farewell = hour < 12 ? "Have a great morning!"
  : "Enjoy your afternoon!";
console.log(farewell);
