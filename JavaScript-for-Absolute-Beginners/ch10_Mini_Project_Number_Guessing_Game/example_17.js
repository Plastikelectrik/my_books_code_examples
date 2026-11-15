// Book: JavaScript for Absolute Beginners — Example 17
// guess.mjs (step 4: input validation)
let tries = 0;
let won = false;

while (tries < MAX_TRIES) {
  const left = MAX_TRIES - tries;
  const answer = await rl.question(
    `Guess (${MIN}-${MAX}), ${left} left: `,
  );
  const guess = Number(answer.trim());

  const isWhole = Number.isInteger(guess);
  const inRange = guess >= MIN && guess <= MAX;
  if (answer.trim() === "" || !isWhole || !inRange) {
    console.log(`Whole numbers ${MIN}-${MAX} only.`);
    continue;
  }

  tries++;

  if (guess === secret) {
    won = true;
    break;
  }
  console.log(guess < secret ? "Higher!" : "Lower!");
}
