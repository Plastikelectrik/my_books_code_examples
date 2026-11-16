// Book: Rust for Beginners — Example 63
fn main() {
    let mut s = String::new();
    let (len, cap) = (s.len(), s.capacity());
    println!("len {len:>2}, capacity {cap:>2}");

    let words = ["Rust", " is", " fast", " and", " safe"];
    for word in words {
        s.push_str(word);
        println!(
            "len {:>2}, capacity {:>2}",
            s.len(),
            s.capacity()
        );
    }
}
