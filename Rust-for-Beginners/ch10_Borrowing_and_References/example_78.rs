// Book: Rust for Beginners — Example 78
fn main() {
    let r = make_string();
    println!("{r}");
}

fn make_string() -> String {
    String::from("temporary") // ownership moves out
}
