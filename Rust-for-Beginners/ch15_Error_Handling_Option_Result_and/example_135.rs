// Book: Rust for Beginners — Example 135
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let width: u32 = "12".parse()?;
    let height: u32 = "x5".parse()?; // fails
    println!("area: {}", width * height);
    Ok(())
}
