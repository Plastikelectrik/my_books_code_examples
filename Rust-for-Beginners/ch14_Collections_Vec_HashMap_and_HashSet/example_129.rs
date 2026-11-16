// Book: Rust for Beginners — Example 129
use std::collections::HashMap;

fn average(grades: &[u32]) -> f64 {
    if grades.is_empty() {
        return 0.0;
    }
    let sum: u32 = grades.iter().sum();
    sum as f64 / grades.len() as f64
}

fn main() {
    let records = [
        ("Ana", 8),
        ("Ben", 6),
        ("Ana", 9),
        ("Cleo", 10),
        ("Ben", 7),
        ("Ana", 7),
    ];

    let mut book: HashMap<&str, Vec<u32>> =
        HashMap::new();
    for (name, grade) in records {
        book.entry(name).or_default().push(grade);
    }

    let mut names: Vec<_> =
        book.keys().copied().collect();
    names.sort();

    for name in names {
        let grades = &book[name];
        println!(
            "{name:<5} {grades:?} average {:.2}",
            average(grades)
        );
    }
}
