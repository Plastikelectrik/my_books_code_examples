// Book: Rust for Beginners — Example 72
fn main() {
    let pair = (String::from("key"), 42);
    let (text, number) = pair; // text takes the String
    println!("{text} -> {number}");
    // pair.0 has been moved, but pair.1 is a Copy i32:
    println!("number is still here: {}", pair.1);
}
