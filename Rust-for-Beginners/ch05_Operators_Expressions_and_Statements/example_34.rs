// Book: Rust for Beginners — Example 34
fn main() {
    let a: u8 = 0b1100;
    let b: u8 = 0b1010;
    println!("a & b  = {:04b}", a & b);
    println!("a | b  = {:04b}", a | b);
    println!("a ^ b  = {:04b}", a ^ b);
    println!("1 << 3 = {}", 1 << 3); // multiply by 8
}
