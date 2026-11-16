// Book: Rust for Beginners — Example 118
fn main() {
    // An empty vector: we must say the type
    let mut tasks: Vec<String> = Vec::new();
    tasks.push(String::from("Write report"));
    tasks.push(String::from("Call Sam"));
    tasks.push(String::from("Buy coffee"));

    // The vec! macro: type inferred from the values
    let primes = vec![2, 3, 5, 7, 11];

    println!("{} tasks: {:?}", tasks.len(), tasks);
    println!("primes: {primes:?}");
}
