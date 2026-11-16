// Book: Rust for Beginners — Example 65
fn main() {
    let a = 10;
    let mut b = a; // copy the value 10 into b

    b += 5;

    println!("a = {a}"); // a is unchanged
    println!("b = {b}");
}
