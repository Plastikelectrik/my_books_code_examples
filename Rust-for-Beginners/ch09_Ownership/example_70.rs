// Book: Rust for Beginners — Example 70
fn main() {
    let s1 = create_greeting(); // ownership moves to s1
    let s2 = String::from("world");
    let s3 = add_exclamation(s2); // in and out

    println!("{s1}");
    println!("{s3}");
}

fn create_greeting() -> String {
    let text = String::from("hello");
    text // ownership moves to the caller
}

fn add_exclamation(mut text: String) -> String {
    text.push('!');
    text // give it back
}
