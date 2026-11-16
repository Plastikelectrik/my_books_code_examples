// Book: Rust for Beginners — Example 186
fn main() {
    let b = Box::new(41);
    let answer = *b + 1; // dereference to reach the value
    println!("b = {b}, answer = {answer}");

    let big = Box::new([0u8; 1_000_000]); // 1 MB
    println!("array length: {}", big.len());
} // b and big are freed here
