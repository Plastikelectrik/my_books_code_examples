// Book: Rust for Beginners — Example 55
fn main() {
    let numbers = [4, 9, 1, 7, 3];
    let (min, max, avg) = statistics(numbers);
    println!("Min: {min}, Max: {max}, Average: {avg:.2}");
}

fn statistics(values: [i32; 5]) -> (i32, i32, f64) {
    let mut min = values[0];
    let mut max = values[0];
    let mut sum = 0;
    for v in values {
        if v < min {
            min = v;
        }
        if v > max {
            max = v;
        }
        sum += v;
    }
    (min, max, sum as f64 / values.len() as f64)
}
