// Book: Rust for Beginners — Example 20
fn main() {
    let letter = 'R';
    let digit = '7';
    let heart = '♥';
    let emoji = '🦀';

    println!("{letter} {digit} {heart} {emoji}");
    println!(
        "Is '7' a digit? {}",
        digit.is_ascii_digit()
    );
    println!(
        "Uppercase 'r': {}",
        'r'.to_ascii_uppercase()
    );
}
