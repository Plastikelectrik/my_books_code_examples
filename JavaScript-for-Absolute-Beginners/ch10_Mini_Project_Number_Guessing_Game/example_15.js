// Book: JavaScript for Absolute Beginners — Example 15
// guess.mjs (step 2)
import * as readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

const rl = readline.createInterface({
  input: stdin,
  output: stdout,
});

const MIN = 1;
const MAX = 50;
const secret =
  Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;
console.log(`(debug) secret is ${secret}`);

const answer = await rl.question("Your guess: ");
const guess = Number(answer);

if (guess === secret) {
  console.log("Correct!");
} else if (guess < secret) {
  console.log("Higher!");
} else {
  console.log("Lower!");
}

rl.close();
