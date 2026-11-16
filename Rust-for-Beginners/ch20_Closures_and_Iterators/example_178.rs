// Book: Rust for Beginners — Example 178
fn main() {
    let fruits = vec!["apple", "kiwi", "plum"];
    let mut it = fruits.iter();

    println!("{:?}", it.next());
    println!("{:?}", it.next());
    println!("{:?}", it.next());
    println!("{:?}", it.next());
}
