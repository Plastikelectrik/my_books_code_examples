// Book: Rust for Beginners — Example 117
#[derive(Debug)]
enum Delivery {
    Ordered,
    Shipped { tracking: String },
    Delivered { signed_by: String },
}

impl Delivery {
    fn advance(self, info: &str) -> Delivery {
        match self {
            Delivery::Ordered => Delivery::Shipped {
                tracking: info.to_string(),
            },
            Delivery::Shipped { .. } => {
                Delivery::Delivered {
                    signed_by: info.to_string(),
                }
            }
            done @ Delivery::Delivered { .. } => done,
        }
    }
}

fn main() {
    let mut d = Delivery::Ordered;
    println!("{d:?}");
    d = d.advance("TRK-123");
    println!("{d:?}");
    d = d.advance("M. Rossi");
    println!("{d:?}");
}
