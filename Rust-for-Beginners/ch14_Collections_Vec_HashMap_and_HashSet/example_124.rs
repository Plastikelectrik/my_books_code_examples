// Book: Rust for Beginners — Example 124
use std::collections::HashMap;

fn main() {
    let mut stock = HashMap::new();
    stock.insert("apples", 12);
    stock.insert("bananas", 0);
    stock.insert("cherries", 40);

    // Collect the keys and sort them for a stable output
    let mut fruits: Vec<_> = stock.keys().collect();
    fruits.sort();

    for fruit in fruits {
        println!("{fruit}: {}", stock[fruit]);
    }
}
