// Book: Rust for Beginners — Example 183
use std::collections::{HashMap, HashSet};

fn main() {
    let words =
        ["apple", "bob", "kayak", "apple", "rust"];

    let unique: HashSet<&str> =
        words.iter().copied().collect();
    let lengths: HashMap<&str, usize> =
        words.iter().map(|w| (*w, w.len())).collect();
    let sentence: String = words.join(" ");
    let upper: Vec<String> =
        words.iter().map(|w| w.to_uppercase()).collect();

    // Collecting Results: stops at the first error
    let parsed: Result<Vec<i32>, _> = ["1", "2", "3"]
        .iter()
        .map(|s| s.parse::<i32>())
        .collect();

    println!("{} unique words", unique.len());
    println!("length of kayak: {}", lengths["kayak"]);
    println!("{sentence}");
    println!("{upper:?}");
    println!("{parsed:?}");
}
