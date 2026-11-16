// Book: Rust for Beginners — Example 238
fn main() {
    let prices = [120.0, 95.5];
    let mut total = 0.0;
    for p in prices {
        total += p;
    }
    let rate = if total >= 200.0 {
        0.15
    } else if total >= 100.0 {
        0.10
    } else {
        0.0
    };
    let final_amount = total * (1.0 - rate);
    println!(
        "Total: {total:.2}, to pay: {final_amount:.2}"
    );
}
