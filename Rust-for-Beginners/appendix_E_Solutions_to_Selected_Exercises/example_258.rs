// Book: Rust for Beginners — Example 258
use std::cell::RefCell;

struct Counter {
    hits: RefCell<u32>,
}

impl Counter {
    fn hit(&self) {
        *self.hits.borrow_mut() += 1;
    }
}

fn main() {
    let c = Counter { hits: RefCell::new(0) };
    let shared = &c;
    for _ in 0..3 {
        shared.hit();
    }
    println!("hits: {}", c.hits.borrow());
}
