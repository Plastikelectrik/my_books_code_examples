// Book: Rust for Beginners — Example 255
use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

#[derive(Debug)]
struct Username(String);

impl From<&str> for Username {
    fn from(s: &str) -> Self {
        Username(s.to_lowercase())
    }
}

fn main() {
    println!("{}", Point { x: 3, y: -4 });
    let u: Username = "AdaL".into();
    println!("{u:?}");
}
