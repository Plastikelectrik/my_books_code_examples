// Book: Rust for Beginners — Example 110
#[derive(Debug)]
enum Payment {
    Cash,
    Card { last_digits: String },
    Transfer { iban: String, reference: String },
}

impl Payment {
    fn fee_cents(&self, amount: u32) -> u32 {
        match self {
            Payment::Cash => 0,
            Payment::Card { .. } => amount * 15 / 1000,
            Payment::Transfer { .. } => 25,
        }
    }

    fn describe(&self) -> String {
        match self {
            Payment::Cash => String::from("cash"),
            Payment::Card { last_digits } => {
                format!("card ending in {last_digits}")
            }
            Payment::Transfer { reference, .. } => {
                format!("transfer, ref {reference}")
            }
        }
    }
}

fn main() {
    let payments = [
        Payment::Cash,
        Payment::Card { last_digits: "4242".into() },
        Payment::Transfer {
            iban: "ES00 0000".into(),
            reference: "INV-77".into(),
        },
    ];
    for p in &payments {
        println!(
            "{}: fee {} cents",
            p.describe(),
            p.fee_cents(10_000)
        );
    }
}
