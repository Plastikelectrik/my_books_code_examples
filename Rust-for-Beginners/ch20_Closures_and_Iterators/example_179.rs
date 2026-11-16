// Book: Rust for Beginners — Example 179
fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    let even_squares: Vec<i32> = numbers
        .iter()
        .filter(|n| *n % 2 == 0) // keep even numbers
        .map(|n| n * n) // square them
        .collect(); // gather into a Vec

    println!("{even_squares:?}");
}
