// Book: Rust for Beginners — Example 40
fn main() {
    // Find the first multiple of 7 greater than 50
    let mut n = 51;
    let found = loop {
        if n % 7 == 0 {
            break n; // the loop's value
        }
        n += 1;
    };
    println!("First multiple of 7 above 50: {found}");
}
