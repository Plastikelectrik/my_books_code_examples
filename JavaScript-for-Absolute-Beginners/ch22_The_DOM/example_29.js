// Book: JavaScript for Absolute Beginners — Example 29
// app.js
const menu = [
  { name: "Latte", price: 3.9, vegan: false,
    soldOut: false },
  { name: "Mocha", price: 4.3, vegan: false,
    soldOut: true },
  { name: "Chai", price: 3.5, vegan: true,
    soldOut: false },
  { name: "Flapjack", price: 2.2, vegan: true,
    soldOut: false },
];

function menuItemElement(item) {
  const li = document.createElement("li");
  li.classList.add("item");
  if (item.vegan) li.classList.add("vegan");
  if (item.soldOut) li.classList.add("sold-out");

  const name = document.createElement("span");
  name.textContent = item.name;

  const price = document.createElement("span");
  price.textContent = item.soldOut
    ? "Sold out"
    : item.price.toFixed(2);

  li.append(name, price);
  return li;
}

function renderMenu(items) {
  const list = document.querySelector("#menu-list");
  list.replaceChildren(...items.map(menuItemElement));
}

renderMenu(menu);
