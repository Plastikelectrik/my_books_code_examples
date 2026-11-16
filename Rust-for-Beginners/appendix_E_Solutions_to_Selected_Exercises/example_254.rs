// Book: Rust for Beginners — Example 254
fn swap_pair<A, B>(pair: (A, B)) -> (B, A) {
    (pair.1, pair.0)
}

fn count_greater<T: PartialOrd>(
    list: &[T],
    limit: &T,
) -> usize {
    list.iter().filter(|x| *x > limit).count()
}

fn main() {
    println!("{:?}", swap_pair(("one", 1)));
    println!("{}", count_greater(&[3, 8, 1, 9, 5], &4));
    println!("{}", count_greater(&["b", "z", "a"], &"m"));
}
