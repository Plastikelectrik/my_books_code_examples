// Book: JavaScript for Absolute Beginners — Example 16
// guess.mjs (step 3: core loop)
const MAX_TRIES = 7;
let won = false;

for (let tryNo = 1; tryNo <= MAX_TRIES; tryNo++) {
  const answer = await rl.question(`Try ${tryNo}: `);
  const guess = Number(answer);

  if (guess === secret) {
    won = true;
    break;
  } else if (guess < secret) {
    console.log("Higher!");
  } else {
    console.log("Lower!");
  }
}

if (won) {
  console.log("You got it!");
} else {
  console.log(`Out of tries! It was ${secret}.`);
}
