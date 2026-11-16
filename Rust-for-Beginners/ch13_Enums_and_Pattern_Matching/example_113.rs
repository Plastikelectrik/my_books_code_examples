// Book: Rust for Beginners — Example 113
fn main() {
    let favorite_color: Option<&str> = Some("teal");
    let lucky_number: Option<u32> = None;

    if let Some(color) = favorite_color {
        println!("Your favorite color is {color}");
    }

    if let Some(n) = lucky_number {
        println!("Your lucky number is {n}");
    } else {
        println!("You have no lucky number");
    }
}
