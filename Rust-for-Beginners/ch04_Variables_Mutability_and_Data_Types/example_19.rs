// Book: Rust for Beginners — Example 19
fn main() {
    let age = 20;
    let is_adult = age >= 18;
    let has_ticket = false;

    println!("Adult: {is_adult}");
    println!("Can enter: {}", is_adult && has_ticket);
}
