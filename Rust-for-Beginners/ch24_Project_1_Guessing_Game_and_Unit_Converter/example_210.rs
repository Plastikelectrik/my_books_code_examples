// Book: Rust for Beginners — Example 210
use std::cmp::Ordering;
use std::io;

fn main() {
    let secret: u32 = 42;
    println!("Guess the number (1-100):");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("read error");

    let guess: u32 = match input.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            println!("That is not a number.");
            return;
        }
    };

    match guess.cmp(&secret) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
