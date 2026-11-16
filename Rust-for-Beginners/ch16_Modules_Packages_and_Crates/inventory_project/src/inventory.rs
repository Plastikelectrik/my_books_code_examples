pub mod item;

use item::Item;

pub struct Inventory {
    items: Vec<Item>,
}

impl Inventory {
    pub fn new() -> Self {
        Inventory { items: Vec::new() }
    }

    pub fn add(&mut self, name: &str, qty: u32) {
        for it in &mut self.items {
            if it.name == name {
                it.qty += qty;
                return;
            }
        }
        self.items.push(Item::new(name, qty));
    }

    pub fn print(&self) {
        for it in &self.items {
            println!("{}", it.describe());
        }
    }
}
