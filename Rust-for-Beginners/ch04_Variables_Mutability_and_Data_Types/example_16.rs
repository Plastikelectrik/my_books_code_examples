// Book: Rust for Beginners — Example 16
fn main() {
    let population = 47_500_000; // easier to read
    let hex = 0xff; // hexadecimal
    let binary = 0b1010; // binary
    let byte = b'A'; // the byte value of a character (u8)
    let small: i8 = -100;

    println!("{population} {hex} {binary}");
    println!("{byte} {small}");
}
