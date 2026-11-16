// Book: Rust for Beginners — Example 241
fn main() {
    for year in [1900, 2000, 2024, 2026] {
        let leap = (year % 4 == 0 && year % 100 != 0)
            || year % 400 == 0;
        println!("{year}: {leap}");
    }
}
