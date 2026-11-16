// Book: Rust for Beginners — Example 82
fn main() {
    let numbers = [10, 20, 30, 40, 50, 60];

    let middle = &numbers[1..4]; // positions 1, 2 and 3
    let start = &numbers[..2]; // from the beginning to 2
    let end = &numbers[4..]; // from 4 to the end
    let all = &numbers[..]; // the whole array

    println!("middle: {middle:?}");
    println!("start:  {start:?}");
    println!("end:    {end:?}");
    println!("all:    {all:?} ({} items)", all.len());
}
