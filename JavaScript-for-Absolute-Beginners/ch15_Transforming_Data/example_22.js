// Book: JavaScript for Absolute Beginners — Example 22
// sales-report.js
const sales = [
  { item: "Latte", type: "drink", qty: 2, price: 3.9 },
  { item: "Scone", type: "food", qty: 1, price: 2.6 },
  { item: "Mocha", type: "drink", qty: 1, price: 4.3 },
  { item: "Latte", type: "drink", qty: 3, price: 3.9 },
  { item: "Flapjack", type: "food", qty: 4, price: 2.2 },
  { item: "Chai", type: "drink", qty: 2, price: 3.5 },
];

const lineTotal = (s) => s.qty * s.price;

const takings =
  sales.reduce((t, s) => t + lineTotal(s), 0);
const itemsSold = sales.reduce((n, s) => n + s.qty, 0);

const qtyByItem = {};
for (const s of sales) {
  qtyByItem[s.item] = (qtyByItem[s.item] ?? 0) + s.qty;
}
const [bestItem, bestQty] = Object.entries(qtyByItem)
  .toSorted((a, b) => b[1] - a[1])[0];

const byType = Object.groupBy(sales, (s) => s.type);
const typeTotals = Object.entries(byType).map(
  ([type, list]) => {
    const total =
      list.reduce((t, s) => t + lineTotal(s), 0);
    return `${type.padEnd(6)} ${total.toFixed(2)}`;
  },
);

console.log("DAILY REPORT");
console.log(`Takings:     ${takings.toFixed(2)}`);
console.log(`Items sold:  ${itemsSold}`);
console.log(`Best seller: ${bestItem} (${bestQty})`);
console.log("By type:");
console.log(typeTotals.map((l) => `  ${l}`).join("\n"));
