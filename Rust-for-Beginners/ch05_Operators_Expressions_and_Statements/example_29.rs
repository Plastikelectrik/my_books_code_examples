// Book: Rust for Beginners — Example 29
fn main() {
    let temperature = 28;
    println!("Hot day: {}", temperature > 25);

    let password = "rustacean";
    println!("Correct: {}", password == "rustacean");

    // Characters and text compare alphabetically
    println!("'a' < 'b': {}", 'a' < 'b');
    println!("apple < banana: {}", "apple" < "banana");
}
