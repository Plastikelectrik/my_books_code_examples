// Book: Rust for Beginners — Example 207
use std::thread;

fn main() {
    let words = vec!["apple", "banana", "cherry", "date"];
    let mut lengths = vec![0; words.len()];

    thread::scope(|s| {
        for (word, slot) in
            words.iter().zip(lengths.iter_mut())
        {
            s.spawn(move || {
                *slot = word.len(); // its own slot
            });
        }
    }); // all threads have finished here

    println!("{words:?}");
    println!("{lengths:?}");
}
