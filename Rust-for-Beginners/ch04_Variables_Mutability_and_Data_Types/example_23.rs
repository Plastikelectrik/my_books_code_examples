// Book: Rust for Beginners — Example 23
fn main() {
    let items: i32 = 7;
    let price: f64 = 2.5;

    // Convert the integer to f64 before multiplying
    let total = items as f64 * price;
    println!("Total: {total}");

    // Converting f64 to an integer cuts the decimals
    let rounded_down = 9.99_f64 as i32;
    println!("9.99 as i32: {rounded_down}");

    // Use round() first if you want normal rounding
    let rounded = 9.99_f64.round() as i32;
    println!("9.99 rounded: {rounded}");
}
