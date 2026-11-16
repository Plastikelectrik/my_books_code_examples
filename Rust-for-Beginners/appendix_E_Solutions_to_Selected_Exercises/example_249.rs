// Book: Rust for Beginners — Example 249
#[derive(Debug)]
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn square(size: f64) -> Self {
        Self { width: size, height: size }
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width
            && self.height > other.height
    }
}

fn main() {
    let big = Rectangle { width: 10.0, height: 8.0 };
    let small = Rectangle::square(5.0);
    println!("{}", big.can_hold(&small));
    println!("{}", small.can_hold(&big));
}
