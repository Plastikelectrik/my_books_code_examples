// Book: Rust for Beginners — Example 201
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..=3 {
            println!("  worker: step {i}");
            thread::sleep(Duration::from_millis(10));
        }
    });

    for i in 1..=3 {
        println!("main: step {i}");
        thread::sleep(Duration::from_millis(10));
    }

    handle.join().unwrap(); // wait for the worker
    println!("both done");
}
