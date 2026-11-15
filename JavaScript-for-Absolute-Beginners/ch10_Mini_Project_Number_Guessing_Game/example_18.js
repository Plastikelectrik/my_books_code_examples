// Book: JavaScript for Absolute Beginners — Example 18
// guess.mjs
import * as readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

const rl = readline.createInterface({
  input: stdin,
  output: stdout,
});

const MIN = 1;
const MAX = 50;
const MAX_TRIES = 7;
const secret =
  Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;

console.log("=================================");
console.log("  COPPER KETTLE GUESSING GAME");
console.log("=================================");
console.log(`I'm thinking of a number ${MIN}-${MAX}.`);
console.log(`You have ${MAX_TRIES} tries. Good luck!\n`);

let tries = 0;
let won = false;

while (tries < MAX_TRIES) {
  const left = MAX_TRIES - tries;
  const answer = await rl.question(
    `Guess (${left} left): `,
  );
  const text = answer.trim();
  const guess = Number(text);

  const isWhole = Number.isInteger(guess);
  const inRange = guess >= MIN && guess <= MAX;
  if (text === "" || !isWhole || !inRange) {
    console.log(`Whole numbers ${MIN}-${MAX} only.`);
    continue;
  }

  tries++;

  if (guess === secret) {
    won = true;
    break;
  }

  const hint = guess < secret ? "Higher!" : "Lower!";
  const close = Math.abs(guess - secret) <= 3;
  console.log(close ? `${hint} So close!` : hint);
}

if (won) {
  const word = tries === 1 ? "try" : "tries";
  console.log(`\nYou got it in ${tries} ${word}!`);
  console.log("Show this code at the counter:");
  console.log(`KETTLE-${secret}${tries}-10OFF`);
} else {
  console.log(`\nOut of tries! It was ${secret}.`);
  console.log("Better luck next time!");
}

rl.close();
