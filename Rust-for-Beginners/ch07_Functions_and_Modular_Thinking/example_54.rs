// Book: Rust for Beginners — Example 54
fn main() {
    println!("{}", safe_divide(10, 2));
    println!("{}", safe_divide(10, 0));
}

fn safe_divide(a: i32, b: i32) -> i32 {
    if b == 0 {
        println!("Warning: division by zero");
        return 0; // exit early
    }
    a / b // normal return value
}
