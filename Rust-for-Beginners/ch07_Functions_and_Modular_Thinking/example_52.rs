// Book: Rust for Beginners — Example 52
fn main() {
    greet("Sofia");
    greet("Liam");
    print_rectangle_area(4, 7);
}

fn greet(name: &str) {
    println!("Welcome, {name}!");
}

fn print_rectangle_area(width: u32, height: u32) {
    let area = width * height;
    println!("{width} x {height} rectangle: area {area}");
}
