// Book: Rust for Beginners — Example 15
fn main() {
    let a = 10; // the compiler infers i32
    let b = 2.5; // the compiler infers f64
    let c: u8 = 200; // we choose the type explicitly
    let d: f32 = 1.5;

    println!("a={a}, b={b}, c={c}, d={d}");
}
