// Book: Rust for Beginners — Example 191
use std::cell::RefCell;

fn main() {
    let data = RefCell::new(vec![1, 2, 3]);

    let reader = data.borrow();
    let writer = data.borrow_mut(); // panics!
    println!("{reader:?} {writer:?}");
}
