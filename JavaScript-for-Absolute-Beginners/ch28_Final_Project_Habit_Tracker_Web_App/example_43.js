// Book: JavaScript for Absolute Beginners — Example 43
// check-habits.mjs
import { createHabit, toggleDay, streak }
  from "./js/habits.js";

const today = new Date(2026, 10, 15);
let water = createHabit("Drink water", "💧");
water = toggleDay(water, "2026-11-13");
water = toggleDay(water, "2026-11-14");
console.log(streak(water, today));

water = toggleDay(water, "2026-11-15");
console.log(streak(water, today));

water = toggleDay(water, "2026-11-14");
console.log(streak(water, today), water.done);
