// Book: Rust for Beginners — Example 79
fn main() {
    let mut counter = 10;

    increment(&mut counter);
    increment(&mut counter);
    println!("counter = {counter}");

    let r = &counter;
    let copy = *r + 1; // read the value behind r
    println!("copy = {copy}");
}

fn increment(n: &mut i32) {
    *n += 1; // change the value that n points to
}
