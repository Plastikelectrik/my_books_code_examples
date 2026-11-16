// Book: Rust for Beginners — Example 190
use std::cell::RefCell;

struct Logger {
    messages: RefCell<Vec<String>>,
}

impl Logger {
    // Note: &self, not &mut self
    fn log(&self, msg: &str) {
        self.messages.borrow_mut().push(msg.to_string());
    }

    fn count(&self) -> usize {
        self.messages.borrow().len()
    }
}

fn main() {
    let logger =
        Logger { messages: RefCell::new(Vec::new()) };
    logger.log("started");
    logger.log("loaded config");
    println!("{} messages", logger.count());
    for m in logger.messages.borrow().iter() {
        println!("- {m}");
    }
}
