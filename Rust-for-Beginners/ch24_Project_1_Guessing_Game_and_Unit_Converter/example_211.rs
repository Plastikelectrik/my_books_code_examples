// Book: Rust for Beginners — Example 211
use std::cmp::Ordering;
use std::io;

fn main() {
    let secret: u32 = 42;
    let mut attempts = 0;
    println!("Guess the number (1-100)!");

    loop {
        println!("Your guess:");
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("read error");

        let guess: u32 = match input.trim().parse() {
            Ok(n) => n,
            Err(_) => {
                println!("Please type a whole number.");
                continue;
            }
        };
        attempts += 1;

        match guess.cmp(&secret) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!(
                    "Correct in {attempts} attempts!"
                );
                break;
            }
        }
    }
}
