// Book: Rust for Beginners — Example 87
fn main() {
    let words = ["hello", "café", "日本", "🦀🦀"];

    for w in words {
        println!(
            "{w}: {} bytes, {} chars",
            w.len(),
            w.chars().count()
        );
    }
}
