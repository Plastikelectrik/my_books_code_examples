// Book: Rust for Beginners — Example 161
fn even_squares(limit: u32) -> impl Iterator<Item = u32> {
    (1..=limit).filter(|n| n % 2 == 0).map(|n| n * n)
}

fn main() {
    for sq in even_squares(10) {
        print!("{sq} ");
    }
    println!();
}
