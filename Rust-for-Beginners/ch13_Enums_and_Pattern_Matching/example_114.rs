// Book: Rust for Beginners — Example 114
fn describe_first_word(text: &str) -> String {
    let Some(word) = text.split_whitespace().next()
    else {
        return String::from("(no words)");
    };
    format!("first word: {word}, {} letters", word.len())
}

fn main() {
    for text in ["hello brave world", "   "] {
        println!("{}", describe_first_word(text));
    }
}
