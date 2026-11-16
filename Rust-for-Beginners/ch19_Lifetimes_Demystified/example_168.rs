// Book: Rust for Beginners — Example 168
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() >= b.len() { a } else { b }
}

fn main() {
    let first = String::from("a long sentence");
    let result;
    {
        let second = String::from("short");
        result = longest(&first, &second);
        println!("longest: {result}");
    }
}
