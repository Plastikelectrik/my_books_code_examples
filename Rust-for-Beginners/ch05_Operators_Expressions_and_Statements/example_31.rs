// Book: Rust for Beginners — Example 31
fn main() {
    let a = 2 + 3 * 4;
    let b = (2 + 3) * 4;
    println!("2 + 3 * 4 = {a}");
    println!("(2 + 3) * 4 = {b}");

    let price = 50.0;
    let discount = 0.2;
    let shipping = 5.0;
    let total = price * (1.0 - discount) + shipping;
    println!("Total: {total}");
}
