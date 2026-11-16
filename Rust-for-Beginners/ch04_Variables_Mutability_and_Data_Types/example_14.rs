// Book: Rust for Beginners — Example 14
fn main() {
    let price = 100;
    let price = price + 21; // a new variable, adding tax
    println!("Price with tax: {price}");

    let input = "42";
    let input: i32 = input.parse().unwrap();
    println!("As a number, doubled: {}", input * 2);
}
