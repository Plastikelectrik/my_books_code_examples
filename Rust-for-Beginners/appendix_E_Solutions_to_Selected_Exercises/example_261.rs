// Book: Rust for Beginners — Example 261
use std::io;

fn main() {
    let mut numbers = Vec::new();
    println!(
        "Type numbers, one per line (empty line ends):"
    );
    loop {
        let mut line = String::new();
        io::stdin()
            .read_line(&mut line)
            .expect("read error");
        let line = line.trim();
        if line.is_empty() {
            break;
        }
        match line.parse::<f64>() {
            Ok(n) => numbers.push(n),
            Err(_) => println!("'{line}' ignored"),
        }
    }
    if numbers.is_empty() {
        println!("No numbers.");
    } else {
        let avg = numbers.iter().sum::<f64>()
            / numbers.len() as f64;
        println!(
            "Average of {}: {avg:.2}",
            numbers.len()
        );
    }
}
