// Book: Rust for Beginners — Example 170
#[derive(Debug)]
struct Highlight<'a> {
    text: &'a str,
    line: usize,
}

fn find_highlights<'a>(
    doc: &'a str,
    word: &str,
) -> Vec<Highlight<'a>> {
    let mut found = Vec::new();
    for (i, line) in doc.lines().enumerate() {
        if line.contains(word) {
            found.push(Highlight {
                text: line,
                line: i + 1,
            });
        }
    }
    found
}

fn main() {
    let document = String::from(
        "Rust is fast.\nRust is safe.\nPython is nice.",
    );
    let hits = find_highlights(&document, "Rust");
    for h in &hits {
        println!("line {}: {}", h.line, h.text);
    }
}
