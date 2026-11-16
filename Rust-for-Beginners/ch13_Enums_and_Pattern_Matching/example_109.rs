// Book: Rust for Beginners — Example 109
#[derive(Debug)]
enum Shape {
    Circle(f64),         // radius
    Rectangle(f64, f64), // width, height
    Triangle { base: f64, height: f64 },
    Point, // no data
}

fn area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle(r) => 3.14159 * r * r,
        Shape::Rectangle(w, h) => w * h,
        Shape::Triangle { base, height } => {
            base * height / 2.0
        }
        Shape::Point => 0.0,
    }
}

fn main() {
    let shapes = vec![
        Shape::Circle(1.0),
        Shape::Rectangle(3.0, 4.0),
        Shape::Triangle { base: 6.0, height: 2.0 },
        Shape::Point,
    ];
    for s in &shapes {
        println!("{s:?} has area {:.2}", area(s));
    }
}
