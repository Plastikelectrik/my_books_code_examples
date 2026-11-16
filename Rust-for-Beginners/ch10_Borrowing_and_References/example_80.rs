// Book: Rust for Beginners — Example 80
fn main() {
    let mut prices = vec![10, 25, 40];

    // Shared borrow: read each element
    for p in &prices {
        println!("Price: {p}");
    }

    // Mutable borrow: change each element
    for p in &mut prices {
        *p += 5; // raise every price by 5
    }

    println!("New prices: {prices:?}");
}
