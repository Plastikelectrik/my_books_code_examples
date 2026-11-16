// Book: Rust for Beginners — Example 33
fn main() {
    let hour = 15;
    let greeting = if hour < 12 {
        "Good morning"
    } else if hour < 20 {
        "Good afternoon"
    } else {
        "Good evening"
    };
    println!("{greeting}!");
}
