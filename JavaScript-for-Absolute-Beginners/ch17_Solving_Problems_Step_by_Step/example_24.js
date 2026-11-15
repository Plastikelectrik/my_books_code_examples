// Book: JavaScript for Absolute Beginners — Example 24
// bake-plan.js
// Inputs: 7 days of sales per pastry.
// Output: how many to bake tomorrow.
// Rule: average + 10%, round up; croissants in 6s.

const sales = {
  scone: [10, 12, 9, 11, 14, 20, 18],
  croissant: [22, 25, 19, 24, 30, 41, 38],
  muffin: [8, 7, 9, 6, 10, 15, 12],
};

for (const [pastry, days] of Object.entries(sales)) {
  console.log(pastry, days.length);
}
