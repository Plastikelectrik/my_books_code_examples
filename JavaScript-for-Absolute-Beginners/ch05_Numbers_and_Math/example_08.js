// Book: JavaScript for Absolute Beginners — Example 08
// receipt.js
const money = new Intl.NumberFormat("en-IE", {
  style: "currency",
  currency: "EUR",
});

// Prices in cents to avoid rounding surprises
const latteCents = 390;
const rollCents = 280;
const toastieCents = 450;

// What table 4 ordered
const lattes = 2;
const rolls = 3;
const toasties = 1;

const latteLine = lattes * latteCents;
const rollLine = rolls * rollCents;
const toastieLine = toasties * toastieCents;

const subtotal = latteLine + rollLine + toastieLine;
const serviceRate = 0.05;
const service = Math.round(subtotal * serviceRate);
const total = subtotal + service;

const show = (cents) => money.format(cents / 100);

console.log("Table 4");
console.log("------------------------------");
console.log(lattes + " x latte      ", show(latteLine));
console.log(rolls + " x roll       ", show(rollLine));
console.log(toasties + " x toastie    ",
  show(toastieLine));
console.log("------------------------------");
console.log("Subtotal      ", show(subtotal));
console.log("Service (5%)  ", show(service));
console.log("TOTAL         ", show(total));
