// Book: Rust for Beginners — Example 53
fn main() {
    let c = 25.0;
    let f = celsius_to_fahrenheit(c);
    println!("{c} °C = {f} °F");
    let boiling = celsius_to_fahrenheit(100.0);
    println!("100 °C = {boiling} °F");
}

fn celsius_to_fahrenheit(celsius: f64) -> f64 {
    celsius * 9.0 / 5.0 + 32.0
}
