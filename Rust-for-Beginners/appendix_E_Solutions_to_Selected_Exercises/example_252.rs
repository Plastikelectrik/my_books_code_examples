// Book: Rust for Beginners — Example 252
use std::collections::{BTreeMap, HashMap};

fn main() {
    // Exercise 3: a BTreeMap keeps the keys sorted
    let mut counts: BTreeMap<char, u32> = BTreeMap::new();
    for c in "mississippi".chars() {
        *counts.entry(c).or_insert(0) += 1;
    }
    println!("{counts:?}");

    // Exercise 5
    let text = "apple avocado banana blueberry cherry";
    let mut groups: HashMap<char, Vec<&str>> =
        HashMap::new();
    for w in text.split_whitespace() {
        let first = w.chars().next().unwrap();
        groups.entry(first).or_default().push(w);
    }
    let mut keys: Vec<_> =
        groups.keys().copied().collect();
    keys.sort();
    for k in keys {
        println!("{k}: {:?}", groups[&k]);
    }
}
