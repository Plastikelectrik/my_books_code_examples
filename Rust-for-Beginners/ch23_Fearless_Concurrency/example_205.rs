// Book: Rust for Beginners — Example 205
use std::sync::Mutex;

fn main() {
    let counter = Mutex::new(0);

    {
        let mut value = counter.lock().unwrap();
        *value += 1;
    } // the lock is released here, automatically

    println!("counter = {:?}", counter.lock().unwrap());
}
