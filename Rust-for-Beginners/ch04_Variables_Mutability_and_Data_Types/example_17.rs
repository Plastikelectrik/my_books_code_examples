// Book: Rust for Beginners — Example 17
fn main() {
    let x: u8 = 250;

    // Wraps around like an odometer
    println!("wrapping:   {}", x.wrapping_add(10));

    // Stops at the maximum value
    println!("saturating: {}", x.saturating_add(10));

    // Returns None when it overflows (see Chapter 15)
    println!("checked:    {:?}", x.checked_add(10));
    println!("checked ok: {:?}", x.checked_add(5));
}
