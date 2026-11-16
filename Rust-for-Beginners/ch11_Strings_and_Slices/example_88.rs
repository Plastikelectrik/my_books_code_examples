// Book: Rust for Beginners — Example 88
fn main() {
    let word = "Señor";

    print!("chars: ");
    for c in word.chars() {
        print!("[{c}] ");
    }
    println!();

    print!("bytes: ");
    for b in word.bytes() {
        print!("{b} ");
    }
    println!();

    // The n-th character (counting from 0)
    let third = word.chars().nth(2);
    println!("third char: {third:?}");
}
