// Book: Rust for Beginners — Example 173
fn main() {
    let double = |x| x * 2;
    let add = |a: i32, b: i32| -> i32 { a + b };
    let greet = || println!("Hello from a closure!");

    println!("double(21) = {}", double(21));
    println!("add(2, 3) = {}", add(2, 3));
    greet();
}
