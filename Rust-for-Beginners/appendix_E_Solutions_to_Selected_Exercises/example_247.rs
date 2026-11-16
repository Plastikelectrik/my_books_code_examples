// Book: Rust for Beginners — Example 247
fn count_char(text: &str, target: char) -> usize {
    text.chars().filter(|c| *c == target).count()
}

fn is_palindrome(text: &str) -> bool {
    text.chars().eq(text.chars().rev())
}

fn initials(full_name: &str) -> String {
    full_name
        .split_whitespace()
        .filter_map(|w| w.chars().next())
        .map(|c| format!("{}.", c.to_uppercase()))
        .collect()
}

fn main() {
    println!("{}", count_char("banana", 'a'));
    println!("{}", is_palindrome("level"));
    println!("{}", is_palindrome("rust"));
    println!("{}", initials("Ada Lovelace"));
}
