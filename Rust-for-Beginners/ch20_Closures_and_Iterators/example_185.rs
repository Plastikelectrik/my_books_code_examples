// Book: Rust for Beginners — Example 185
use std::collections::HashMap;

struct Sale {
    product: &'static str,
    region: &'static str,
    units: u32,
    unit_price: f64,
}

fn sale(
    product: &'static str,
    region: &'static str,
    units: u32,
    unit_price: f64,
) -> Sale {
    Sale { product, region, units, unit_price }
}

fn main() {
    let sales = vec![
        sale("laptop", "north", 3, 899.0),
        sale("mouse", "south", 25, 19.5),
        sale("laptop", "south", 2, 899.0),
        sale("screen", "north", 7, 179.0),
        sale("mouse", "north", 40, 19.5),
    ];

    let revenue =
        |s: &Sale| s.units as f64 * s.unit_price;

    let total: f64 = sales.iter().map(revenue).sum();
    println!("Total revenue: {total:.2}");

    let best = sales
        .iter()
        .max_by(|a, b| revenue(a).total_cmp(&revenue(b)))
        .unwrap();
    println!(
        "Best sale: {} in {}",
        best.product, best.region
    );

    let mut by_region: HashMap<&str, f64> =
        HashMap::new();
    for s in &sales {
        *by_region.entry(s.region).or_insert(0.0) +=
            revenue(s);
    }
    let mut regions: Vec<_> =
        by_region.into_iter().collect();
    regions.sort_by(|a, b| b.1.total_cmp(&a.1));
    for (region, amount) in &regions {
        println!("{region:<6} {amount:>9.2}");
    }

    let big_orders: Vec<_> = sales
        .iter()
        .filter(|s| s.units >= 10)
        .map(|s| format!("{} x{}", s.product, s.units))
        .collect();
    println!("Big orders: {}", big_orders.join(", "));
}
