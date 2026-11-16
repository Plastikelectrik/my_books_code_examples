// Book: Rust for Beginners — Example 165
#[derive(Debug)]
struct Celsius(f64);

#[derive(Debug)]
struct Fahrenheit(f64);

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self {
        Fahrenheit(c.0 * 9.0 / 5.0 + 32.0)
    }
}

fn main() {
    let boiling = Fahrenheit::from(Celsius(100.0));
    let body: Fahrenheit = Celsius(37.0).into();
    println!("{boiling:?}");
    println!("{body:?}");
}
