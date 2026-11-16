// Book: Rust for Beginners — Example 58
fn main() {
    let prices = [19.99, 5.49, 42.0];
    let mut t = 0.0;
    for p in prices {
        t += p;
    }
    let t2 = if t > 50.0 { t * 0.9 } else { t };
    let t3 = t2 * 1.21;
    println!("Total: {:.2}", t3);
}
