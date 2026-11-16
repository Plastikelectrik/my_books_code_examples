// Book: Rust for Beginners — Example 174
fn main() {
    let tax_rate = 0.21;
    let with_tax = |price: f64| price * (1.0 + tax_rate);

    println!("{:.2}", with_tax(100.0));
    println!("{:.2}", with_tax(19.99));
}
