import { brewTime } from "./brew.mjs";

const teas = ["green", "black", "oolong", "herbal",
              "mint"];
for (const tea of teas) {
  for (let s = 1; s <= 5; s++) {
    console.log(`${tea},${s},${brewTime(tea, s)}`);
  }
}
