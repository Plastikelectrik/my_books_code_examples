// Book: Rust for Beginners — Example 10
fn main() {
    let prices = [35.0, 42.5, 29.9];

    // Accumulate the total
    let mut total = 0.0;
    for p in prices {
        total += p;
    }

    // Decide whether the discount applies
    let final_amount = if total >= 100.0 {
        total - total * 0.10
    } else {
        total
    };

    println!("Total before discount: {total:.2}");
    println!("Amount to pay: {final_amount:.2}");
}
