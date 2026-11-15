// Book: JavaScript for Absolute Beginners — Example 06
// specials-board-v2.js
const cafeName = "THE COPPER KETTLE CAFE";

const lattePrice = 3.9;
const matchaPrice = 3.5;
const rollPrice = 2.8;
const toastiePrice = 4.5;

const comboDiscount = 0.1; // 10% off
const comboPrice =
  (lattePrice + rollPrice) * (1 - comboDiscount);

console.log("==============================");
console.log(cafeName);
console.log("==============================");
console.log("Pumpkin spice latte ....", lattePrice);
console.log("Iced matcha ............", matchaPrice);
console.log("Cinnamon roll ..........", rollPrice);
console.log("Cheese toastie .........", toastiePrice);
console.log("Combo (latte + roll) ...", comboPrice);
