// Book: Rust for Beginners — Example 06
fn main() {
    let numbers = [12, 45, 7, 89, 23, 61];

    // Step 1: the first number is the largest so far
    let mut largest = numbers[0];

    // Steps 2-4: look at every number
    for n in numbers {
        if n > largest {
            largest = n; // remember the bigger one
        }
    }

    // Step 5: the answer
    println!("The largest number is {largest}");
}
