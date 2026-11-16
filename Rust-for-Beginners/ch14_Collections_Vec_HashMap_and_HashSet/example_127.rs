// Book: Rust for Beginners — Example 127
use std::collections::HashSet;

fn main() {
    let visits = [
        "home", "about", "home", "blog", "about", "home",
    ];

    let mut unique = HashSet::new();
    for page in visits {
        let is_new = unique.insert(page);
        if is_new {
            println!("first visit to {page}");
        }
    }
    println!("{} visits", visits.len());
    println!("{} unique pages", unique.len());
    println!("visited blog? {}", unique.contains("blog"));
}
