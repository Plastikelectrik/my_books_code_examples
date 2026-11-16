// Book: Rust for Beginners — Example 243
fn main() {
    let mut n = 101;
    let found = loop {
        if n % 6 == 0 && n % 8 == 0 {
            break n;
        }
        n += 1;
    };
    println!("{found}");
}
