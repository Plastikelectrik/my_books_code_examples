// Book: JavaScript for Absolute Beginners — Example 13
// ask.mjs
import * as readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

const rl = readline.createInterface({
  input: stdin,
  output: stdout,
});

const name = await rl.question("What's your name? ");
console.log(`Nice to meet you, ${name}!`);

rl.close();
