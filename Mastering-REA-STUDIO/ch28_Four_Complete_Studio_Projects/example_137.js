Java.perform(() => {
  const Calc = Java.use(
    "com.example.kettle.BrewCalculator");
  const calc = Calc.INSTANCE.value;
  const teas = ["green", "black", "oolong", "herbal",
                "mint"];
  for (const tea of teas) {
    for (let s = 1; s <= 5; s++) {
      console.log(`${tea},${s},${calc.brewTime(tea, s)}`);
    }
  }
});
