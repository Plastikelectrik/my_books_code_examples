// Book: Rust for Beginners — Example 85
fn main() {
    let literal: &str = "I live inside the program";
    let owned = String::from("I live on the heap");

    // A &str can be turned into a String...
    let from_literal: String = literal.to_string();

    // ...and a String can be viewed as a &str
    let view: &str = &owned;

    println!("{literal}");
    println!("{owned}");
    println!("{from_literal}");
    println!("{view}");
}
