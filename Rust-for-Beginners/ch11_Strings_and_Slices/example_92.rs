// Book: Rust for Beginners — Example 92
fn main() {
    let text = "  The Rust Book is a great book  ";

    let clean = text.trim();
    println!("trim:        '{clean}'");
    println!("upper:       {}", clean.to_uppercase());
    println!("lower:       {}", clean.to_lowercase());
    println!("contains:    {}", clean.contains("Rust"));
    println!("starts_with: {}", clean.starts_with("The"));
    println!("ends_with:   {}", clean.ends_with("book"));
    println!("find:        {:?}", clean.find("Book"));
    println!("find (none): {:?}", clean.find("Python"));
    let replaced = clean.replace("book", "read");
    println!("replace:     {replaced}");
}
