// Book: JavaScript for Absolute Beginners — Example 09
// kitchen-ticket.js
const rawName = "   sam  ";
const rawDrink = "  OAT Flat WHITE ";
const rawNote = "extra hot   -  no foam  ";
const table = 7;

const name = rawName.trim().toUpperCase();
const drink = rawDrink.trim().toLowerCase();

// Collapse repeated spaces: split on spaces,
// drop the empty pieces, join with one space.
const note = rawNote
  .trim()
  .split(" ")
  .filter((word) => word !== "")
  .join(" ");

const width = 30;
const line = "-".repeat(width);
const ticketNo = String(table).padStart(3, "0");

console.log(line);
console.log(`TICKET #${ticketNo}`.padStart(width));
console.log(line);
console.log("Name:  " + name);
console.log("Drink: " + drink);
console.log("Note:  " + note);
console.log(line);
