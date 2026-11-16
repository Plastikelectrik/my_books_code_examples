// Book: Rust for Beginners — Example 202
use std::thread;

fn main() {
    let numbers: Vec<u64> = (1..=1_000_000).collect();
    let (first, second) =
        numbers.split_at(numbers.len() / 2);
    let first = first.to_vec();
    let second = second.to_vec();

    let h1 =
        thread::spawn(move || first.iter().sum::<u64>());
    let h2 =
        thread::spawn(move || second.iter().sum::<u64>());

    let total = h1.join().unwrap() + h2.join().unwrap();
    println!("total = {total}");
}
