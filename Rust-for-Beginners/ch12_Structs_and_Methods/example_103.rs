// Book: Rust for Beginners — Example 103
#[derive(Debug)]
struct Temperature {
    celsius: f64,
}

impl Temperature {
    fn new(celsius: f64) -> Self {
        Self { celsius }
    }

    fn from_fahrenheit(f: f64) -> Self {
        Self { celsius: (f - 32.0) * 5.0 / 9.0 }
    }

    fn fahrenheit(&self) -> f64 {
        self.celsius * 9.0 / 5.0 + 32.0
    }
}

fn main() {
    let today = Temperature::new(22.0);
    let oven = Temperature::from_fahrenheit(392.0);

    println!(
        "Today: {} °C = {} °F",
        today.celsius,
        today.fahrenheit()
    );
    println!("Oven: {} °C", oven.celsius);
}
