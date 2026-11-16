// Book: Rust for Beginners — Example 169
fn first_word<'a>(
    text: &'a str,
    _separator: &str,
) -> &'a str {
    text.split_whitespace().next().unwrap_or("")
}

fn main() {
    let sentence = String::from("hello brave world");
    let word;
    {
        let sep = String::from(" ");
        word = first_word(&sentence, &sep);
    } // sep dropped: fine, the result does not borrow it
    println!("first word: {word}");
}
