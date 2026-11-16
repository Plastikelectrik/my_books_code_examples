// Book: Rust for Beginners — Example 18
fn main() {
    let pi = 3.14159; // f64 by default
    let radius: f64 = 2.0;
    let area = pi * radius * radius;
    println!("Area of the circle: {area:.3}");

    // Floating-point numbers are approximations
    let sum = 0.1 + 0.2;
    println!("0.1 + 0.2 = {sum}");
}
