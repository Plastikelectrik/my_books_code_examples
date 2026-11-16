// Book: Rust for Beginners — Example 248
fn main() {
    let text = "name=Alice;age=30;city=Paris";
    for pair in text.split(';') {
        if let Some((key, value)) = pair.split_once('=') {
            println!("{key} -> {value}");
        }
    }
}
