// Book: Rust for Beginners — Example 181
fn main() {
    let names = ["Ana", "Ben", "Cleo", "Dev"];
    let ages = [31, 25, 42, 19];

    // zip: combine two sequences
    for (name, age) in names.iter().zip(ages.iter()) {
        print!("{name}={age} ");
    }
    println!();

    // skip, take and rev
    let middle: Vec<_> =
        (1..=10).skip(2).take(4).collect();
    let countdown: Vec<_> = (1..=5).rev().collect();
    println!("{middle:?} {countdown:?}");

    // filter_map: parse, keeping only valid numbers
    let raw = ["4", "x", "15", "", "8"];
    let valid: Vec<i32> = raw
        .iter()
        .filter_map(|s| s.parse().ok())
        .collect();
    println!("{valid:?}");

    // flat_map: all characters of all names
    let letters: String =
        names.iter().flat_map(|n| n.chars()).collect();
    println!("{letters}");
}
