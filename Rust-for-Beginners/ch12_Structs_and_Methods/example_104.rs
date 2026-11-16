// Book: Rust for Beginners — Example 104
#[derive(Debug)]
struct Color(u8, u8, u8);

#[derive(Debug)]
struct Meters(f64);

fn main() {
    let orange = Color(217, 72, 15);
    let distance = Meters(42.195);

    println!("{orange:?}, red = {}", orange.0);
    println!("{distance:?}, value = {}", distance.0);
}
