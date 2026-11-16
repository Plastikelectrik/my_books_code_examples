// Book: Rust for Beginners — Example 164
use std::fmt;

struct Money {
    cents: i64,
    currency: &'static str,
}

impl fmt::Display for Money {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let sign = if self.cents < 0 { "-" } else { "" };
        let abs = self.cents.abs();
        write!(
            f,
            "{sign}{}.{:02} {}",
            abs / 100,
            abs % 100,
            self.currency
        )
    }
}

fn main() {
    let price = Money { cents: 129_900, currency: "EUR" };
    let refund = Money { cents: -450, currency: "USD" };

    println!("Price: {price}");
    println!("Refund: {refund}");
    let text: String = price.to_string();
    println!("As text: '{text}'");
}
