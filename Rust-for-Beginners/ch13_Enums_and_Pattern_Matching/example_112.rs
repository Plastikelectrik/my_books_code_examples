// Book: Rust for Beginners — Example 112
fn main() {
    let numbers = vec![10, 20, 30];

    println!("first: {:?}", numbers.first());
    println!("get(1): {:?}", numbers.get(1));
    println!("get(9): {:?}", numbers.get(9));
    println!("max: {:?}", numbers.iter().max());

    let empty: Vec<i32> = Vec::new();
    println!("max of empty: {:?}", empty.iter().max());
}
