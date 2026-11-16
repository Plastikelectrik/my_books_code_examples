// Book: Rust for Beginners — Example 123
use std::collections::HashMap;

fn main() {
    let mut capitals = HashMap::new();
    capitals.insert("France", "Paris");
    capitals.insert("Japan", "Tokyo");
    capitals.insert("Kenya", "Nairobi");

    // Look up a value: returns an Option
    match capitals.get("Japan") {
        Some(city) => println!("Japan: {city}"),
        None => println!("Unknown"),
    }

    let peru = capitals.contains_key("Peru");
    println!("Has Peru? {peru}");
    println!("Number of entries: {}", capitals.len());

    capitals.remove("Kenya");
    println!("After removing Kenya: {}", capitals.len());
}
