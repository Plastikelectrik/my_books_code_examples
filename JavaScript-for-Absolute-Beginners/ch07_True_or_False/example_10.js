// Book: JavaScript for Absolute Beginners — Example 10
// cafe-status.js
const day = "Saturday";
const hour = 10;
const croissantsLeft = 0;

const isWeekend = day === "Saturday" || day === "Sunday";

const opensAt = isWeekend ? 9 : 7;
const closesAt = 18;
const isOpen = hour >= opensAt && hour < closesAt;

const breakfastUntil = 11;
const servingBreakfast = isOpen && hour < breakfastUntil;

const isHappyHour = isOpen && hour >= 15 && hour < 17;
const hasCroissants = croissantsLeft > 0;

console.log(`Day: ${day}, ${hour}:00`);
console.log(`Open now:          ${isOpen}`);
console.log(`Serving breakfast: ${servingBreakfast}`);
console.log(`Happy hour:        ${isHappyHour}`);
console.log(`Croissants left:   ${hasCroissants}`);
