// Book: Rust for Beginners — Example 144
use std::collections::HashMap;
use std::fmt::Write as _;

mod geometry {
    pub mod shapes {
        pub fn square_area(side: f64) -> f64 {
            side * side
        }
    }
}

use geometry::shapes;
use geometry::shapes::square_area;

fn main() {
    let mut m = HashMap::new();
    m.insert("a", 1);

    println!("{}", geometry::shapes::square_area(2.0));
    println!("{}", shapes::square_area(3.0));
    println!("{}", square_area(4.0));

    let mut report = String::new();
    let _ = write!(report, "{} entries", m.len());
    println!("{report}");
}
