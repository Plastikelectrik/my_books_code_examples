// Book: Rust for Beginners — Example 96
struct Book {
    title: String,
    author: String,
    year: u16,
    available: bool,
}

fn main() {
    let book = Book {
        title: String::from("Dune"),
        author: String::from("Frank Herbert"),
        year: 1965,
        available: true,
    };

    println!("{} by {}", book.title, book.author);
    println!("Published: {}", book.year);
    println!("Available: {}", book.available);
}
