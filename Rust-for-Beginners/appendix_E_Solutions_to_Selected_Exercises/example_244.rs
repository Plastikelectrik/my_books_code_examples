// Book: Rust for Beginners — Example 244
fn max_of_three(a: i32, b: i32, c: i32) -> i32 {
    a.max(b).max(c)
}

fn sum_to(n: u32) -> u32 {
    if n == 0 { 0 } else { n + sum_to(n - 1) }
}

fn main() {
    println!("{}", max_of_three(4, 19, 7));
    println!("{}", sum_to(100));
}
