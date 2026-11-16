// Book: Rust for Beginners — Example 66
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // ownership moves to s2
    println!("{s2}, world!");
}
