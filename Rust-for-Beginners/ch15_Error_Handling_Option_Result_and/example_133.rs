// Book: Rust for Beginners — Example 133
use std::num::ParseIntError;

fn sum_of_two(
    a: &str,
    b: &str,
) -> Result<i32, ParseIntError> {
    let x: i32 = a.parse()?; // return early on error
    let y: i32 = b.parse()?;
    Ok(x + y)
}

fn main() {
    println!("{:?}", sum_of_two("10", "32"));
    println!("{:?}", sum_of_two("10", "abc"));
}
