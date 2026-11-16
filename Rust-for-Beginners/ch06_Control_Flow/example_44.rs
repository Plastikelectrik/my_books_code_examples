// Book: Rust for Beginners — Example 44
fn main() {
    let podium = ["Ana", "Ben", "Chen"];

    for (i, name) in podium.iter().enumerate() {
        println!("Position {}: {name}", i + 1);
    }
}
