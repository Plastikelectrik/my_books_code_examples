// Book: Rust for Beginners — Example 90
fn main() {
    let mut s = String::new(); // empty

    s.push_str("Rust"); // add text
    s.push(' '); // add one character
    s.push_str("2024");
    println!("1: {s}");

    s.insert_str(0, "Learning "); // at byte 0
    println!("2: {s}");

    s.replace_range(9..13, "RUST"); // replace bytes 9..13
    println!("3: {s}");

    let last = s.pop(); // remove the last character
    println!("4: {s} (removed {last:?})");

    s.truncate(13); // keep only the first 13 bytes
    println!("5: {s}");

    s.clear(); // remove everything
    println!("6: '{s}' is empty: {}", s.is_empty());
}
