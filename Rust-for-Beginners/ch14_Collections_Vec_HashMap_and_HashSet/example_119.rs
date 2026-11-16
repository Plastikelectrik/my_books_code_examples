// Book: Rust for Beginners — Example 119
fn main() {
    let colors = vec!["red", "green", "blue"];

    // Indexing: panics if the index is out of range
    let second = colors[1];
    println!("second: {second}");

    // get: returns an Option, never panics
    match colors.get(5) {
        Some(c) => println!("sixth: {c}"),
        None => println!("there is no sixth color"),
    }

    println!("first: {:?}", colors.first());
    println!("last: {:?}", colors.last());
}
