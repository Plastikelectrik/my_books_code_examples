// Book: Rust for Beginners — Example 150
fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];
    for &item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn main() {
    let numbers = [34, 50, 25, 100, 65];
    let decimals = [1.5, 0.3, 9.9, 4.2];
    let letters = ['r', 'u', 's', 't'];

    println!("largest number: {}", largest(&numbers));
    println!("largest decimal: {}", largest(&decimals));
    println!("largest letter: {}", largest(&letters));
}
