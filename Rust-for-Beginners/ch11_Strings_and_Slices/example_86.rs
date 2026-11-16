// Book: Rust for Beginners — Example 86
fn greet(name: &str) {
    println!("Hello, {name}!");
}

fn main() {
    let owned = String::from("Maria");

    greet("Tom"); // a literal (&str)
    greet(&owned); // &String becomes &str automatically
    greet(&owned[..3]); // a slice of the String
}
