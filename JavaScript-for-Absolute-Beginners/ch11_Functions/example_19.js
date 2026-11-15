// Book: JavaScript for Absolute Beginners — Example 19
// cafe-toolkit.js
const PRICES = { small: 2.8, medium: 3.4, large: 3.9 };

function basePrice(size) {
  return PRICES[size] ?? PRICES.medium;
}

function isOpen(day, hour) {
  const weekend = day === "Saturday" || day === "Sunday";
  const opensAt = weekend ? 9 : 7;
  return hour >= opensAt && hour < 18;
}

function memberDiscount(price, isMember) {
  return isMember ? price * 0.9 : price;
}

function formatPrice(amount) {
  return `${amount.toFixed(2)} €`;
}

function quote(size, isMember) {
  const price = memberDiscount(basePrice(size), isMember);
  return `${size} coffee: ${formatPrice(price)}`;
}

console.log(isOpen("Sunday", 8));
console.log(isOpen("Monday", 8));
console.log(quote("large", true));
console.log(quote("small", false));
console.log(quote("gigantic", false));
