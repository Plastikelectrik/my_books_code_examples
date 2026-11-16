// Book: Rust for Beginners — Example 196
pub struct Percentage(u8);

impl Percentage {
    pub fn new(value: u8) -> Percentage {
        if value > 100 {
            panic!(
                "percentage must be 0-100, got {value}"
            );
        }
        Percentage(value)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn accepts_100() {
        assert_eq!(Percentage::new(100).0, 100);
    }

    #[test]
    #[should_panic(expected = "must be 0-100")]
    fn rejects_101() {
        Percentage::new(101);
    }
}
