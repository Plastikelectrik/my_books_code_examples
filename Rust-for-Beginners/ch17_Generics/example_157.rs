// Book: Rust for Beginners — Example 157
#[derive(Debug)]
struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        Stack { items: Vec::new() }
    }

    fn push(&mut self, item: T) {
        self.items.push(item);
    }

    fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }

    fn peek(&self) -> Option<&T> {
        self.items.last()
    }

    fn len(&self) -> usize {
        self.items.len()
    }

    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }
}

fn main() {
    // A stack of numbers
    let mut numbers = Stack::new();
    numbers.push(1);
    numbers.push(2);
    numbers.push(3);
    println!(
        "top: {:?}, size: {}",
        numbers.peek(),
        numbers.len()
    );

    // A stack of text: an "undo" history
    let mut history: Stack<String> = Stack::new();
    history.push("typed 'Hello'".to_string());
    history.push("made it bold".to_string());

    while let Some(action) = history.pop() {
        println!("undo: {action}");
    }
    println!("history empty? {}", history.is_empty());
}
