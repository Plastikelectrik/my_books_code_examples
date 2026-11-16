// Book: Rust for Beginners — Example 245
fn shout(text: String) -> String {
    format!("{}!", text.to_uppercase())
}

fn main() {
    let word = String::from("hello");
    let loud = shout(word);
    println!("{loud}");
    // word cannot be used here: it was moved into shout
}
