// Book: Rust for Beginners — Example 171
fn default_greeting() -> &'static str {
    "Hello, stranger!" // a literal lives forever
}

fn level_name(level: u8) -> &'static str {
    match level {
        0 => "beginner",
        1 => "intermediate",
        _ => "expert",
    }
}

fn main() {
    let g = default_greeting();
    println!("{g}");
    for lvl in 0..3 {
        println!("level {lvl}: {}", level_name(lvl));
    }
}
