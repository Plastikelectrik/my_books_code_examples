// Book: Rust for Beginners — Example 162
trait Shape {
    fn area(&self) -> f64;
    fn name(&self) -> String;
}

struct Circle {
    radius: f64,
}
struct Square {
    side: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }
    fn name(&self) -> String {
        format!("circle (r={})", self.radius)
    }
}

impl Shape for Square {
    fn area(&self) -> f64 {
        self.side * self.side
    }
    fn name(&self) -> String {
        format!("square (side={})", self.side)
    }
}

fn main() {
    let shapes: Vec<Box<dyn Shape>> = vec![
        Box::new(Circle { radius: 1.0 }),
        Box::new(Square { side: 2.0 }),
        Box::new(Circle { radius: 0.5 }),
    ];

    let mut total = 0.0;
    for s in &shapes {
        println!(
            "{:<18} area {:>6.2}",
            s.name(),
            s.area()
        );
        total += s.area();
    }
    println!("total area: {total:.2}");
}
