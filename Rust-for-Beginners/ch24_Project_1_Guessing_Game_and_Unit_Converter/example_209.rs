// Book: Rust for Beginners — Example 209
use std::io;

fn main() {
    println!("What is your name?");

    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read line");

    let name = name.trim();
    println!("Nice to meet you, {name}!");
}
