// Book: Rust for Beginners — Example 237
fn main() {
    let numbers = [12, 45, 7, 89, 23, 61];
    let mut smallest = numbers[0];
    for n in numbers {
        if n < smallest {
            smallest = n;
        }
    }
    println!("The smallest number is {smallest}");
}
