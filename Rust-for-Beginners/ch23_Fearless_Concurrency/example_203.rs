// Book: Rust for Beginners — Example 203
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let messages =
            ["download started", "50%", "100%", "done"];
        for m in messages {
            tx.send(m.to_string()).unwrap();
        }
        // tx is dropped here: the channel closes
    });

    // The receiver works like an iterator
    for msg in rx {
        println!("got: {msg}");
    }
    println!("channel closed");
}
