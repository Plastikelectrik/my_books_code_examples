// Book: Rust for Beginners — Example 12
fn main() {
    let mut lives = 3;
    println!("Lives: {lives}");

    lives = 2; // allowed, because lives is mutable
    println!("Lives: {lives}");

    lives -= 1; // subtract 1
    println!("Lives: {lives}");
}
