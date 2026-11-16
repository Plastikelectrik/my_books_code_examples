// Book: Rust for Beginners — Example 81
fn main() {
    let mut text = String::from("Rust is fast");

    print_stats(&text);
    append_sentence(&mut text, "Rust is safe");
    append_sentence(&mut text, "Rust is fun");
    print_stats(&text);

    println!("Final text: {text}");
}

fn count_words(t: &String) -> usize {
    t.split_whitespace().count()
}

fn count_vowels(t: &String) -> usize {
    let mut count = 0;
    for c in t.chars() {
        if "aeiouAEIOU".contains(c) {
            count += 1;
        }
    }
    count
}

fn print_stats(t: &String) {
    println!(
        "{} chars, {} words, {} vowels",
        t.len(),
        count_words(t),
        count_vowels(t)
    );
}

fn append_sentence(t: &mut String, sentence: &str) {
    t.push_str(". ");
    t.push_str(sentence);
}
