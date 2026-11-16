// Book: Rust for Beginners — Example 43
fn main() {
    // Multiplication table of 7
    for i in 1..=10 {
        println!("7 x {i} = {}", 7 * i);
    }

    // Countdown with rev()
    for i in (1..=3).rev() {
        print!("{i} ");
    }
    println!("go!");
}
