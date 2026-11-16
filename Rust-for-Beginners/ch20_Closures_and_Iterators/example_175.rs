// Book: Rust for Beginners — Example 175
fn main() {
    let mut count = 0;
    let mut increment = || {
        count += 1; // needs &mut count
        println!("count is now {count}");
    };

    increment();
    increment();
    // count is borrowed until the closure's last use
    println!("final count: {count}");
}
