use std::env;
use std::fmt;
use std::io::{self, Write};

#[derive(Debug, Clone, Copy, PartialEq)]
enum Category {
    Length,
    Weight,
    Temperature,
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Unit {
    Meter,
    Kilometer,
    Mile,
    Foot,
    Gram,
    Kilogram,
    Pound,
    Ounce,
    Celsius,
    Fahrenheit,
    Kelvin,
}

impl Unit {
    const ALL: [Unit; 11] = [
        Unit::Meter,
        Unit::Kilometer,
        Unit::Mile,
        Unit::Foot,
        Unit::Gram,
        Unit::Kilogram,
        Unit::Pound,
        Unit::Ounce,
        Unit::Celsius,
        Unit::Fahrenheit,
        Unit::Kelvin,
    ];

    fn symbol(self) -> &'static str {
        match self {
            Unit::Meter => "m",
            Unit::Kilometer => "km",
            Unit::Mile => "mi",
            Unit::Foot => "ft",
            Unit::Gram => "g",
            Unit::Kilogram => "kg",
            Unit::Pound => "lb",
            Unit::Ounce => "oz",
            Unit::Celsius => "c",
            Unit::Fahrenheit => "f",
            Unit::Kelvin => "k",
        }
    }

    fn category(self) -> Category {
        use Unit::*;
        match self {
            Meter | Kilometer | Mile | Foot => {
                Category::Length
            }
            Gram | Kilogram | Pound | Ounce => {
                Category::Weight
            }
            Celsius | Fahrenheit | Kelvin => {
                Category::Temperature
            }
        }
    }

    /// Factor to the base unit (meters or grams).
    fn factor(self) -> f64 {
        match self {
            Unit::Meter | Unit::Gram => 1.0,
            Unit::Kilometer | Unit::Kilogram => 1000.0,
            Unit::Mile => 1609.344,
            Unit::Foot => 0.3048,
            Unit::Pound => 453.59237,
            Unit::Ounce => 28.349523125,
            _ => 1.0, // temperatures use formulas
        }
    }

    fn parse(text: &str) -> Result<Unit, ConvError> {
        let t = text.trim().to_lowercase();
        Unit::ALL
            .iter()
            .copied()
            .find(|u| u.symbol() == t)
            .ok_or(ConvError::UnknownUnit(t))
    }
}

#[derive(Debug, PartialEq)]
enum ConvError {
    UnknownUnit(String),
    BadNumber(String),
    Incompatible(Unit, Unit),
    BelowAbsoluteZero,
}

impl fmt::Display for ConvError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ConvError::UnknownUnit(u) => {
                write!(f, "unknown unit '{u}'")
            }
            ConvError::BadNumber(n) => {
                write!(f, "'{n}' is not a number")
            }
            ConvError::Incompatible(a, b) => write!(
                f,
                "cannot convert {} to {}",
                a.symbol(),
                b.symbol()
            ),
            ConvError::BelowAbsoluteZero => {
                write!(f, "below absolute zero")
            }
        }
    }
}

fn to_celsius(value: f64, from: Unit) -> f64 {
    match from {
        Unit::Fahrenheit => (value - 32.0) * 5.0 / 9.0,
        Unit::Kelvin => value - 273.15,
        _ => value,
    }
}

fn from_celsius(c: f64, to: Unit) -> f64 {
    match to {
        Unit::Fahrenheit => c * 9.0 / 5.0 + 32.0,
        Unit::Kelvin => c + 273.15,
        _ => c,
    }
}

/// Converts between two units of the same category.
fn convert(
    value: f64,
    from: Unit,
    to: Unit,
) -> Result<f64, ConvError> {
    if from.category() != to.category() {
        return Err(ConvError::Incompatible(from, to));
    }
    if from.category() == Category::Temperature {
        let c = to_celsius(value, from);
        if c < -273.15 {
            return Err(ConvError::BelowAbsoluteZero);
        }
        return Ok(from_celsius(c, to));
    }
    Ok(value * from.factor() / to.factor())
}

/// Parses "10", "km", "mi" and converts.
fn run(
    value: &str,
    from: &str,
    to: &str,
) -> Result<String, ConvError> {
    let v: f64 = value.trim().parse().map_err(|_| {
        ConvError::BadNumber(value.trim().to_string())
    })?;
    let (f, t) = (Unit::parse(from)?, Unit::parse(to)?);
    let result = convert(v, f, t)?;
    Ok(format!(
        "{v} {} = {result:.4} {}",
        f.symbol(),
        t.symbol()
    ))
}

fn ask(prompt: &str) -> String {
    print!("{prompt}");
    io::stdout().flush().expect("flush failed");
    let mut line = String::new();
    io::stdin()
        .read_line(&mut line)
        .expect("read failed");
    line.trim().to_string()
}

fn interactive() {
    let symbols: Vec<&str> =
        Unit::ALL.iter().map(|u| u.symbol()).collect();
    println!("=== UNIT CONVERTER ===");
    println!("Units: {}", symbols.join(", "));
    println!(
        "Type: <value> <from> <to>   (or 'q' to quit)"
    );
    loop {
        let line = ask("> ");
        if line.is_empty() {
            continue;
        }
        if line == "q" || line == "quit" {
            break;
        }
        let parts: Vec<&str> =
            line.split_whitespace().collect();
        if parts.len() != 3 {
            println!("Example: 10 km mi");
            continue;
        }
        match run(parts[0], parts[1], parts[2]) {
            Ok(text) => println!("{text}"),
            Err(e) => println!("Error: {e}"),
        }
    }
    println!("Goodbye!");
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    match args.as_slice() {
        [] => interactive(),
        [value, from, to] => match run(value, from, to) {
            Ok(text) => println!("{text}"),
            Err(e) => {
                eprintln!("Error: {e}");
                std::process::exit(1);
            }
        },
        _ => {
            eprintln!(
                "Usage: converter [<value> <from> <to>]"
            );
            std::process::exit(2);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn close(a: f64, b: f64) -> bool {
        (a - b).abs() < 1e-6
    }

    #[test]
    fn length_conversions() {
        let mi =
            convert(10.0, Unit::Kilometer, Unit::Mile);
        assert!(close(mi.unwrap(), 6.213712));
        let ft = convert(1.0, Unit::Meter, Unit::Foot);
        assert!(close(ft.unwrap(), 3.280840));
    }

    #[test]
    fn temperature_conversions() {
        let f = convert(
            100.0,
            Unit::Celsius,
            Unit::Fahrenheit,
        );
        assert!(close(f.unwrap(), 212.0));
        let k =
            convert(32.0, Unit::Fahrenheit, Unit::Kelvin);
        assert!(close(k.unwrap(), 273.15));
    }

    #[test]
    fn errors_are_reported() {
        assert_eq!(
            convert(1.0, Unit::Gram, Unit::Mile),
            Err(ConvError::Incompatible(
                Unit::Gram,
                Unit::Mile
            ))
        );
        assert_eq!(
            convert(-300.0, Unit::Celsius, Unit::Kelvin),
            Err(ConvError::BelowAbsoluteZero)
        );
        assert!(matches!(
            Unit::parse("parsec"),
            Err(ConvError::UnknownUnit(_))
        ));
    }
}
