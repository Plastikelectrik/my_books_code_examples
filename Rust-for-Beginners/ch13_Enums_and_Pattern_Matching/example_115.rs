// Book: Rust for Beginners — Example 115
fn main() {
    let some_age: Option<u32> = Some(29);
    let no_age: Option<u32> = None;

    println!("{}", some_age.unwrap_or(0));
    println!("{}", no_age.unwrap_or(0));
    println!("{:?}", some_age.map(|a| a + 1));
    println!("{:?}", no_age.map(|a| a + 1));
    println!("{}", no_age.is_none());
}
