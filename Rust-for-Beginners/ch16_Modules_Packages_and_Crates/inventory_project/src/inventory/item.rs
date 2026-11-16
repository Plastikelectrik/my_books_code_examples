pub struct Item {
    pub name: String,
    pub qty: u32,
}

impl Item {
    pub fn new(name: &str, qty: u32) -> Self {
        Item { name: name.to_string(), qty }
    }

    pub fn describe(&self) -> String {
        format!("{:<8} x{}", self.name, self.qty)
    }
}
