// Book: Rust for Beginners — Example 35
fn main() {
    let x: i32 = -7;
    println!("abs(-7) = {}", x.abs());
    println!("2 to the power 10 = {}", 2_i32.pow(10));
    println!("max(3, 9) = {}", 3.max(9));
    println!("min(3, 9) = {}", 3.min(9));

    let y: f64 = 2.0;
    println!("sqrt(2) = {:.4}", y.sqrt());
    println!("3.7 floor = {}", 3.7_f64.floor());
    println!("3.2 ceil = {}", 3.2_f64.ceil());
    println!("2.5 round = {}", 2.5_f64.round());
}
