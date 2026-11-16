// Book: Rust for Beginners — Example 156
use std::fmt::Display;

fn print_summary<T, U>(title: T, items: &[U]) -> usize
where
    T: Display,
    U: Display + PartialOrd,
{
    println!("== {title} ==");
    for item in items {
        println!("- {item}");
    }
    items.len()
}

fn main() {
    let n = print_summary("Scores", &[88, 92, 75]);
    println!("({n} items)");
    print_summary(2026, &["alpha", "beta"]);
}
