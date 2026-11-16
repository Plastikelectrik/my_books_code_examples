// Book: Rust for Beginners — Example 155
#[derive(Debug)]
struct Point<T> {
    x: T,
    y: T,
}

// Methods for every Point<T>
impl<T> Point<T> {
    fn new(x: T, y: T) -> Self {
        Point { x, y }
    }

    fn x(&self) -> &T {
        &self.x
    }
}

// Methods only for Point<f64>
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x * self.x + self.y * self.y).sqrt()
    }
}

fn main() {
    let p = Point::new(3.0, 4.0);
    let q = Point::new('a', 'b');

    println!("p.x = {}", p.x());
    println!("q.x = {}", q.x());
    println!("distance = {}", p.distance_from_origin());
    // q.distance_from_origin(); // error: only for f64
}
