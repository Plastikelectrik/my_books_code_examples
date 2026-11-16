// Book: Rust for Beginners — Example 200
//! Temperature conversions and classifications.

/// Converts degrees Celsius to degrees Fahrenheit.
pub fn c_to_f(c: f64) -> f64 {
    c * 9.0 / 5.0 + 32.0
}

/// Converts degrees Fahrenheit to degrees Celsius.
pub fn f_to_c(f: f64) -> f64 {
    (f - 32.0) * 5.0 / 9.0
}

/// Describes how a temperature in Celsius feels.
pub fn feels_like(c: f64) -> &'static str {
    match c {
        t if t < 0.0 => "freezing",
        t if t < 15.0 => "cold",
        t if t < 25.0 => "pleasant",
        _ => "hot",
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn close(a: f64, b: f64) -> bool {
        (a - b).abs() < 1e-9
    }

    #[test]
    fn known_conversion_points() {
        assert!(close(c_to_f(0.0), 32.0));
        assert!(close(c_to_f(100.0), 212.0));
        assert!(close(c_to_f(-40.0), -40.0));
    }

    #[test]
    fn conversions_are_inverse() {
        for c in [-20.0, 0.0, 21.5, 37.0, 100.0] {
            assert!(
                close(f_to_c(c_to_f(c)), c),
                "failed for {c}"
            );
        }
    }

    #[test]
    fn classification_boundaries() {
        assert_eq!(feels_like(-0.1), "freezing");
        assert_eq!(feels_like(0.0), "cold");
        assert_eq!(feels_like(15.0), "pleasant");
        assert_eq!(feels_like(25.0), "hot");
    }
}
