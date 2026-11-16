// Book: Rust for Beginners — Example 91
fn main() {
    let first = String::from("Grace");
    let last = "Hopper";

    // 1. format! (does not take ownership of anything)
    let full = format!("{first} {last}");
    println!("{full}");

    // 2. The + operator (moves the left side)
    let greeting = String::from("Hello, ") + &full + "!";
    println!("{greeting}");

    // 3. Joining a list of pieces
    let parts = ["red", "green", "blue"];
    println!("{}", parts.join(", "));

    // first and full are still usable here
    println!("{first} / {full}");
}
