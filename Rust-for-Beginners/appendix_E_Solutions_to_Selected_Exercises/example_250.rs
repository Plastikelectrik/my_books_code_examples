// Book: Rust for Beginners — Example 250
fn divide(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 { None } else { Some(a / b) }
}

fn main() {
    match divide(10.0, 4.0) {
        Some(r) => println!("result: {r}"),
        None => println!("cannot divide by zero"),
    }
    println!("{}", divide(1.0, 0.0).unwrap_or(f64::NAN));
}
