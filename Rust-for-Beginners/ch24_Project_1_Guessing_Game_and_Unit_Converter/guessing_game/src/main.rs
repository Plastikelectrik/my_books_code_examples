use std::cmp::Ordering;
use std::io::{self, Write};

const MIN: u32 = 1;
const MAX: u32 = 100;
const MAX_ATTEMPTS: u32 = 7;

/// Prints a prompt and returns the trimmed line typed.
fn ask(prompt: &str) -> String {
    print!("{prompt}");
    io::stdout().flush().expect("cannot flush stdout");
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("read error");
    line.trim().to_string()
}

/// Asks until the user types a number inside the range.
fn read_guess() -> u32 {
    loop {
        let text = ask("Your guess: ");
        match text.parse::<u32>() {
            Ok(n) if (MIN..=MAX).contains(&n) => {
                return n;
            }
            Ok(_) => {
                println!("Stay between {MIN} and {MAX}.")
            }
            Err(_) => {
                println!("'{text}' is not a number.")
            }
        }
    }
}

/// Plays one round. Returns true if the player won.
fn play_round() -> bool {
    let secret = rand::random_range(MIN..=MAX);
    println!(
        "\nI am thinking of a number from {MIN} to {MAX}."
    );
    println!("You have {MAX_ATTEMPTS} attempts.");

    for attempt in 1..=MAX_ATTEMPTS {
        let guess = read_guess();
        match guess.cmp(&secret) {
            Ordering::Less => println!("  Higher!"),
            Ordering::Greater => println!("  Lower!"),
            Ordering::Equal => {
                println!(
                    "  Correct! Found in {attempt} tries."
                );
                return true;
            }
        }
        let left = MAX_ATTEMPTS - attempt;
        if left > 0 {
            println!("  {left} attempts left.");
        }
    }
    println!("Out of attempts! The number was {secret}.");
    false
}

fn main() {
    println!("=== GUESS THE NUMBER ===");
    let mut wins = 0;
    let mut rounds = 0;

    loop {
        rounds += 1;
        if play_round() {
            wins += 1;
        }
        println!(
            "Score: {wins} wins in {rounds} rounds."
        );

        let again =
            ask("Play again? (y/n): ").to_lowercase();
        if again != "y" && again != "yes" {
            break;
        }
    }
    println!("Thanks for playing!");
}
