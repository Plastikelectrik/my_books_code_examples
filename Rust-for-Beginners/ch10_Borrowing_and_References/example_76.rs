// Book: Rust for Beginners — Example 76
fn main() {
    let text = String::from("shared");
    let r1 = &text;
    let r2 = &text;
    let r3 = &text;
    println!("{r1}, {r2}, {r3}");
}
