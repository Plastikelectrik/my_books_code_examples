// Book: Rust for Beginners — Example 102
#[derive(Debug)]
struct Order {
    items: Vec<String>,
    paid: bool,
}

impl Order {
    // &self: read only
    fn count(&self) -> usize {
        self.items.len()
    }

    // &mut self: modify
    fn add(&mut self, item: &str) {
        self.items.push(item.to_string());
    }

    // self: consume the order and produce a receipt
    fn pay(self) -> String {
        let n = self.items.len();
        format!("Receipt: {n} items paid")
    }
}

fn main() {
    let mut order =
        Order { items: Vec::new(), paid: false };
    order.add("coffee");
    order.add("croissant");
    println!("{} items", order.count());
    println!("paid: {}", order.paid);

    let receipt = order.pay(); // order is moved here
    println!("{receipt}");
    // order.add("tea"); // error: order was moved
}
