// Book: Rust for Beginners — Example 62
fn main() {
    let mut message = String::from("Hello");
    println!("{message} (length {})", message.len());

    message.push_str(", Rust");
    message.push('!');
    println!("{message} (length {})", message.len());
}
