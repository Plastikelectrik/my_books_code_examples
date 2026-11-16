// Book: Rust for Beginners — Example 217
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 3, y: -7 };

    let json = serde_json::to_string(&p).unwrap();
    println!("to JSON:   {json}");

    let back: Point =
        serde_json::from_str(&json).unwrap();
    println!("from JSON: {back:?}");
}
