// Book: Rust for Beginners — Example 95
fn longest_word(text: &str) -> &str {
    let mut longest = "";
    for word in text.split_whitespace() {
        let n = word.chars().count();
        if n > longest.chars().count() {
            longest = word;
        }
    }
    longest
}

fn capitalize(word: &str) -> String {
    let mut chars = word.chars();
    match chars.next() {
        Some(first) => {
            first.to_uppercase().collect::<String>()
                + chars.as_str()
        }
        None => String::new(),
    }
}

fn main() {
    let sentence = "rust gives programmers superpowers";

    println!("Sentence: {sentence}");
    let count = sentence.split_whitespace().count();
    println!("Words: {count}");
    println!("Longest word: {}", longest_word(sentence));

    let title: Vec<String> = sentence
        .split_whitespace()
        .map(capitalize)
        .collect();
    println!("Title case: {}", title.join(" "));
}
