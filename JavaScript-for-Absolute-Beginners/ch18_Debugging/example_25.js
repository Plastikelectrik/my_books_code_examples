// Book: JavaScript for Absolute Beginners — Example 25
// buggy-total.js
function orderTotal(items, isMember) {
  let total = 0;
  for (const item of items) {
    let price = item.price * item.qty;
    if (isMember && item.type === "drink") {
      price = price * 0.1;
    }
    total += price;
  }
  return total;
}

const order = [
  { name: "Latte", type: "drink", price: 3.9, qty: 2 },
  { name: "Scone", type: "food", price: 2.6, qty: 1 },
];

console.log(orderTotal(order, false).toFixed(2));
console.log(orderTotal(order, true).toFixed(2));
