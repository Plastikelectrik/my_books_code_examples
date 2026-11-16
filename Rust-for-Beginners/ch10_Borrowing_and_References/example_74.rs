// Book: Rust for Beginners — Example 74
fn main() {
    let s1 = String::from("ownership");
    let len = calculate_length(&s1); // lend s1
    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
} // s goes out of scope, but it owns nothing,
// so nothing is dropped
