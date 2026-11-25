Java.perform(() => {
  const Calc = Java.use(
    "com.example.kettle.BrewCalculator");
  Calc.brewTime.implementation = function (tea, s) {
    const r = this.brewTime(tea, s);
    console.log(`brewTime(${tea}, ${s}) = ${r}`);
    return r;
  };
});
