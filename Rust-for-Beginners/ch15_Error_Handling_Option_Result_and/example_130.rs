// Book: Rust for Beginners — Example 130
fn set_volume(level: u8) {
    if level > 100 {
        panic!("volume must be 0-100, got {level}");
    }
    println!("Volume set to {level}");
}

fn main() {
    set_volume(40);
    set_volume(150);
    println!("This line never runs");
}
