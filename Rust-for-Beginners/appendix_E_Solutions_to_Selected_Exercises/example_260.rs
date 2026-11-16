// Book: Rust for Beginners — Example 260
use std::sync::{Arc, Mutex, mpsc};
use std::thread;

fn main() {
    // Exercise 3
    let (tx, rx) = mpsc::channel();
    for p in 0..3 {
        let tx = tx.clone();
        thread::spawn(move || {
            for i in 1..=5 {
                tx.send(p * 10 + i).unwrap();
            }
        });
    }
    drop(tx);
    let total: i32 = rx.iter().sum();
    println!("total: {total}");

    // Exercise 4
    let log = Arc::new(Mutex::new(Vec::new()));
    let handles: Vec<_> = (0..4)
        .map(|id| {
            let log = Arc::clone(&log);
            thread::spawn(move || {
                log.lock()
                    .unwrap()
                    .push(format!("thread {id}"));
            })
        })
        .collect();
    for h in handles {
        h.join().unwrap();
    }
    let mut entries = log.lock().unwrap().clone();
    entries.sort();
    println!("{entries:?}");
}
