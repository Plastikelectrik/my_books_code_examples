// Book: Rust for Beginners — Example 151
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn main() {
    let words = vec![
        String::from("apple"),
        String::from("pear"),
        String::from("banana"),
    ];
    println!("largest word: {}", largest(&words));
    println!("largest number: {}", largest(&[3, 9, 2]));
}
