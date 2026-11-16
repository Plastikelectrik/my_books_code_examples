// Book: Rust for Beginners — Example 61
use std::mem::size_of;

fn main() {
    println!("u8:        {} byte", size_of::<u8>());
    println!("i32:       {} bytes", size_of::<i32>());
    println!("f64:       {} bytes", size_of::<f64>());
    println!("char:      {} bytes", size_of::<char>());
    println!("bool:      {} byte", size_of::<bool>());
    let array = size_of::<[i32; 5]>();
    let tuple = size_of::<(u8, f64)>();
    println!("[i32; 5]:  {array} bytes");
    println!("(u8, f64): {tuple} bytes");
}
