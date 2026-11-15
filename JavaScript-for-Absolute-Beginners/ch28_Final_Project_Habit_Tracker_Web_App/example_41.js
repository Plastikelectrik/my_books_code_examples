// Book: JavaScript for Absolute Beginners — Example 41
// check-dates.mjs
import { dateKey, addDays, lastDays }
  from "./js/dates.js";

const d = new Date(2026, 11, 31); // 31 December 2026
console.log(dateKey(d));
console.log(dateKey(addDays(d, 1)));
console.log(lastDays(3, d).map((x) => dateKey(x)));
