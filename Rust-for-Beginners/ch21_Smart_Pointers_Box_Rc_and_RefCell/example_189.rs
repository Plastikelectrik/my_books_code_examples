// Book: Rust for Beginners — Example 189
use std::rc::Rc;

#[derive(Debug)]
struct Image {
    name: String,
    size_kb: u32,
}

fn main() {
    let logo = Rc::new(Image {
        name: "logo.png".into(),
        size_kb: 120,
    });
    println!("owners: {}", Rc::strong_count(&logo));

    let header = Rc::clone(&logo); // a new owner, no copy
    let footer = Rc::clone(&logo);
    println!("owners: {}", Rc::strong_count(&logo));

    println!("header shows {}", header.name);
    println!(
        "footer shows {} ({} KB)",
        footer.name, footer.size_kb
    );

    drop(header); // one owner less
    println!("owners: {}", Rc::strong_count(&logo));
}
