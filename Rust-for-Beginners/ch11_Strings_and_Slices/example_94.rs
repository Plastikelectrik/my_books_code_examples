// Book: Rust for Beginners — Example 94
fn main() {
    let input = "42";
    let n: i32 = input.parse().unwrap();
    println!("{n} + 8 = {}", n + 8);

    let price: f64 = " 19.95 ".trim().parse().unwrap();
    println!("price with tax: {:.2}", price * 1.21);

    let bad = "forty-two".parse::<i32>();
    println!("parsing 'forty-two': {bad:?}");

    let back_to_text: String = n.to_string();
    println!("as text: '{back_to_text}'");
}
