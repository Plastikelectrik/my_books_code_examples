// Book: Rust for Beginners — Example 08
fn main() {
    let age = 70;

    let price = if age < 12 {
        5
    } else if age >= 65 {
        6
    } else {
        9
    };

    println!("Age {age}: the ticket costs {price} euros");
}
