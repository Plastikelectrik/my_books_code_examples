// Book: Rust for Beginners — Example 166
use std::ops::Add;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Vector2 {
    x: f64,
    y: f64,
}

impl Add for Vector2 {
    type Output = Vector2;

    fn add(self, other: Vector2) -> Vector2 {
        Vector2 {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    let position = Vector2 { x: 1.0, y: 2.0 };
    let velocity = Vector2 { x: 0.5, y: -1.0 };
    let next = position + velocity;
    println!("{next:?}");
}
