// Book: Rust for Beginners — Example 131
fn main() {
    let inputs = ["42", "-7", "seven", "99999999999"];

    for text in inputs {
        match text.parse::<i32>() {
            Ok(n) => println!("'{text}' -> {n}"),
            Err(e) => println!("'{text}' -> error: {e}"),
        }
    }
}
