// Book: Rust for Beginners — Example 134
fn initials(full_name: &str) -> Option<String> {
    let mut parts = full_name.split_whitespace();
    let first = parts.next()?.chars().next()?;
    let last = parts.last()?.chars().next()?;
    Some(format!("{first}.{last}."))
}

fn main() {
    println!("{:?}", initials("Grace Brewster Hopper"));
    println!("{:?}", initials("Plato"));
    println!("{:?}", initials(""));
}
