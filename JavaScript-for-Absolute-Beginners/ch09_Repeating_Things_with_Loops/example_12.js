// Book: JavaScript for Absolute Beginners — Example 12
// loyalty.js
const coffeePrice = 3.2;
const visits = 25;
const freeEvery = 10;

let paid = 0;
let freeCoffees = 0;
let card = "";

for (let visit = 1; visit <= visits; visit++) {
  if (visit % freeEvery === 0) {
    freeCoffees++;
    card += "★";
    console.log(`Visit ${visit}: FREE coffee! ${card}`);
    card = "";
    continue;
  }
  paid += coffeePrice;
  card += "●";
}

const saved = freeCoffees * coffeePrice;
console.log(`Paid: ${paid.toFixed(2)}`);
console.log(`Free coffees: ${freeCoffees}`);
console.log(`Saved: ${saved.toFixed(2)}`);
console.log(`Card now: ${card}`);
