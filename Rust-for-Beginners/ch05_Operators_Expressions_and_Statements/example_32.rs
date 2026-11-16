// Book: Rust for Beginners — Example 32
fn main() {
    let total = {
        let base = 40;
        let tax = base * 21 / 100;
        base + tax // no semicolon: block value
    };
    println!("Total with tax: {total}");
}
