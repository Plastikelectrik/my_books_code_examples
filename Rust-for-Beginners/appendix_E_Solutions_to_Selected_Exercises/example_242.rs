// Book: Rust for Beginners — Example 242
fn main() {
    for row in 1..=5 {
        for _ in 0..row {
            print!("*");
        }
        println!();
    }
}
