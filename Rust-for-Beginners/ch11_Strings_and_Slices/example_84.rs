// Book: Rust for Beginners — Example 84
fn main() {
    let mut scores = [50, 60, 70, 80, 90];

    let last_three = &mut scores[2..];
    for s in last_three {
        *s += 5; // bonus for the last three
    }

    println!("{scores:?}");
}
