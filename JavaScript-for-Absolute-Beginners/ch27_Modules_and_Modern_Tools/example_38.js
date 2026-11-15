// Book: JavaScript for Absolute Beginners — Example 38
// js/main.js
import { MENU } from "./data.js";
import { renderMenu, renderBasket } from "./render.js";
import { createBasket } from "./basket.js";
import { showWeatherTip } from "./weather.js";

const basket = createBasket();

renderMenu(MENU);
renderBasket(basket.lines());

document.querySelector("#menu-list")
  .addEventListener("click", (event) => {
    const li = event.target.closest(".item");
    if (!li) return;
    const name = li.dataset.name;
    basket.add(MENU.find((m) => m.name === name));
    renderBasket(basket.lines());
  });

showWeatherTip();
