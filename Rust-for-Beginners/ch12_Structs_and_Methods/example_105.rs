// Book: Rust for Beginners — Example 105
#[derive(Debug)]
struct Address {
    street: String,
    city: String,
}

#[derive(Debug)]
struct Customer {
    name: String,
    address: Address,
    points: u32,
}

impl Customer {
    fn label(&self) -> String {
        format!(
            "{}\n{}\n{}",
            self.name,
            self.address.street,
            self.address.city
        )
    }
}

fn main() {
    let c = Customer {
        name: String::from("Lena Fischer"),
        address: Address {
            street: String::from("12 River Road"),
            city: String::from("Bristol"),
        },
        points: 120,
    };
    println!("{}", c.label());
    println!("Points: {}", c.points);
}
