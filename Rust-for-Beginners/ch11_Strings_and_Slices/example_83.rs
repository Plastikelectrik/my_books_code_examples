// Book: Rust for Beginners — Example 83
fn sum(values: &[i32]) -> i32 {
    let mut total = 0;
    for v in values {
        total += v;
    }
    total
}

fn main() {
    let array = [1, 2, 3, 4, 5];
    let vector = vec![10, 20, 30];

    println!("whole array: {}", sum(&array));
    println!("first three: {}", sum(&array[..3]));
    println!("vector:      {}", sum(&vector));
}
