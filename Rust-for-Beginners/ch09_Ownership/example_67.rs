// Book: Rust for Beginners — Example 67
fn main() {
    let s1 = String::from("hello");
    let mut s2 = s1.clone(); // a full copy, heap included

    s2.push_str(" there");

    println!("s1 = {s1}");
    println!("s2 = {s2}");
}
