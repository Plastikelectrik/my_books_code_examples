// Book: Rust for Beginners — Example 59
const VAT_RATE: f64 = 0.21;
const DISCOUNT_LIMIT: f64 = 50.0;
const DISCOUNT_RATE: f64 = 0.10;

fn main() {
    let prices = [19.99, 5.49, 42.0];
    let subtotal = sum(prices);
    let discounted = apply_discount(subtotal);
    let total = add_vat(discounted);
    println!("Total: {total:.2}");
}

fn sum(values: [f64; 3]) -> f64 {
    let mut total = 0.0;
    for v in values {
        total += v;
    }
    total
}

fn apply_discount(amount: f64) -> f64 {
    if amount > DISCOUNT_LIMIT {
        amount * (1.0 - DISCOUNT_RATE)
    } else {
        amount
    }
}

fn add_vat(amount: f64) -> f64 {
    amount * (1.0 + VAT_RATE)
}
