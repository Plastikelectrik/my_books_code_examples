// Book: Rust for Beginners — Example 239
fn main() {
    for c in [0.0, 100.0, -40.0] {
        let f: f64 = c * 9.0 / 5.0 + 32.0;
        println!("{c} °C = {f} °F");
    }
}
