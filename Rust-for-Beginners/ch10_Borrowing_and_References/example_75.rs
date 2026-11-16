// Book: Rust for Beginners — Example 75
fn main() {
    let mut s = String::from("hello");
    add_world(&mut s);
    add_world(&mut s);
    println!("{s}");
}

fn add_world(text: &mut String) {
    text.push_str(", world");
}
