// Book: Rust for Beginners — Example 125
use std::collections::HashMap;

fn main() {
    let text = "the cat and the dog and the bird";
    let mut counts: HashMap<&str, u32> = HashMap::new();

    for word in text.split_whitespace() {
        let count = counts.entry(word).or_insert(0);
        *count += 1;
    }

    let mut words: Vec<_> = counts.into_iter().collect();
    // Sort by count (highest first), then alphabetically
    words
        .sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(b.0)));

    for (word, n) in words {
        println!("{word:<5} {n}");
    }
}
