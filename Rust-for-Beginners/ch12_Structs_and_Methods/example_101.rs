// Book: Rust for Beginners — Example 101
#[derive(Debug)]
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    fn is_square(&self) -> bool {
        self.width == self.height
    }
}

fn main() {
    let r = Rectangle { width: 8.0, height: 5.0 };
    println!("{r:?}");
    println!("Area: {}", r.area());
    println!("Perimeter: {}", r.perimeter());
    println!("Square? {}", r.is_square());
}
