// Book: Rust for Beginners — Example 30
fn main() {
    let age = 16;
    let with_parent = true;
    let is_holiday = false;

    let can_enter = age >= 18 || with_parent;
    let free_entry = age < 12 && !is_holiday;

    println!("Can enter: {can_enter}");
    println!("Free entry: {free_entry}");
}
