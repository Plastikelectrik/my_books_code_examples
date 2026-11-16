// Book: Rust for Beginners — Example 256
fn make_counter() -> impl FnMut() -> u32 {
    let mut count = 0;
    move || {
        count += 1;
        count
    }
}

fn main() {
    let sum: u32 = (1..100)
        .filter(|n| n % 2 == 1)
        .map(|n| n * n)
        .sum();
    println!("sum of odd squares: {sum}");

    let mut next = make_counter();
    println!("{} {} {}", next(), next(), next());

    let a = [1, 2, 3];
    let b = [4, 5, 6];
    let dot: i32 =
        a.iter().zip(b.iter()).map(|(x, y)| x * y).sum();
    println!("dot product: {dot}");
}
