// Book: Rust for Beginners — Example 57
fn main() {
    for n in 1..=6 {
        println!("{n}! = {}", factorial(n));
    }
}

fn factorial(n: u64) -> u64 {
    if n <= 1 {
        1 // base case: stop here
    } else {
        n * factorial(n - 1) // recursive case
    }
}
