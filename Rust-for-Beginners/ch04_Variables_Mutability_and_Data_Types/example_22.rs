// Book: Rust for Beginners — Example 22
fn main() {
    let days = ["Mon", "Tue", "Wed", "Thu", "Fri"];
    let temperatures: [i32; 5] = [18, 21, 19, 24, 22];
    let zeros = [0; 4]; // four zeros

    println!("First day: {}", days[0]);
    println!("Last day: {}", days[4]);
    println!("Number of days: {}", days.len());
    println!("Temperatures: {:?}", temperatures);
    println!("Zeros: {:?}", zeros);
}
