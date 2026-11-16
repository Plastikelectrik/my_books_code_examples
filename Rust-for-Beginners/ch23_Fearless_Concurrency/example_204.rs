// Book: Rust for Beginners — Example 204
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    for id in 1..=3 {
        let tx = tx.clone(); // one sender per worker
        thread::spawn(move || {
            let result = id * id;
            tx.send((id, result)).unwrap();
        });
    }
    drop(tx); // drop the original, or rx never ends

    let mut results: Vec<(i32, i32)> =
        rx.iter().collect();
    results.sort();
    for (id, r) in results {
        println!("worker {id} computed {r}");
    }
}
