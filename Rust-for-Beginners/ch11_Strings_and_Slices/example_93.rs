// Book: Rust for Beginners — Example 93
fn main() {
    let csv_line = "Lisbon,Portugal,545000";
    for field in csv_line.split(',') {
        println!("field: {field}");
    }

    let sentence = "the quick   brown fox";
    let words: Vec<&str> =
        sentence.split_whitespace().collect();
    println!("words: {words:?}");

    let poem = "line one\nline two\nline three";
    for (n, line) in poem.lines().enumerate() {
        println!("{}: {line}", n + 1);
    }
}
