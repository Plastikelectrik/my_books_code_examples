// Book: Rust for Beginners — Example 121
fn main() {
    let mut scores = vec![70, 85, 92];

    for s in &scores {
        // shared borrow: read
        print!("{s} ");
    }
    println!();

    for s in &mut scores {
        // mutable borrow: modify
        *s += 5;
    }
    println!("{scores:?}");

    for s in scores {
        // take ownership: the vector is consumed
        print!("[{s}] ");
    }
    println!();
    // scores can no longer be used here
}
