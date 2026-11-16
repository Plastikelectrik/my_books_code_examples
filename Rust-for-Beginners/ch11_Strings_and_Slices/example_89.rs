// Book: Rust for Beginners — Example 89
fn main() {
    let text = "Hello, world";
    let hello = &text[0..5];
    let world = &text[7..];
    println!("{hello} | {world}");

    let spanish = "año";
    println!("{}", &spanish[0..1]); // "a", 1 byte
    // &spanish[0..2] would panic: byte 2 is inside 'ñ'
    println!("{}", &spanish[0..3]); // "añ", 3 bytes
}
