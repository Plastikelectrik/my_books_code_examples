// Book: JavaScript for Absolute Beginners — Example 34
// money.js
const symbol = "€";

export function formatPrice(amount) {
  return `${amount.toFixed(2)} ${symbol}`;
}

export function addTax(amount, rate = 0.21) {
  return amount * (1 + rate);
}
