// Book: Rust for Beginners — Example 122
#[derive(Debug)]
struct Product {
    name: String,
    price_cents: u32,
    stock: u32,
}

impl Product {
    fn new(name: &str, price: u32, stock: u32) -> Self {
        let name = name.to_string();
        Self { name, price_cents: price, stock }
    }
}

fn main() {
    let mut inventory = vec![
        Product::new("Pen", 150, 40),
        Product::new("Notebook", 450, 0),
        Product::new("Stapler", 899, 7),
    ];

    inventory.push(Product::new("Ruler", 120, 15));

    let mut total_value = 0;
    for p in &inventory {
        total_value += p.price_cents * p.stock;
        if p.stock == 0 {
            println!("Out of stock: {}", p.name);
        }
    }
    println!("Inventory value: {} cents", total_value);

    // Sort by price, cheapest first
    inventory.sort_by_key(|p| p.price_cents);
    for p in &inventory {
        println!("{:<10} {:>5}", p.name, p.price_cents);
    }
}
