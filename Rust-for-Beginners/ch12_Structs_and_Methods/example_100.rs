// Book: Rust for Beginners — Example 100
#[derive(Debug)]
struct Point {
    x: f64,
    y: f64,
}

fn main() {
    let p = Point { x: 3.5, y: -1.0 };
    println!("{p:?}");
    println!("{p:#?}");
}
