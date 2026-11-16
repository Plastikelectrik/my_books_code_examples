// Book: Rust for Beginners — Example 27
fn main() {
    let n = 2026;
    println!("{n} is even: {}", n % 2 == 0);
    println!("Last digit of {n}: {}", n % 10);

    let total_minutes = 135;
    let hours = total_minutes / 60;
    let minutes = total_minutes % 60;
    println!("{total_minutes} = {hours}h {minutes}min");
}
