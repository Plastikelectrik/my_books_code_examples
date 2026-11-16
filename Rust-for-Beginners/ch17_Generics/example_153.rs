// Book: Rust for Beginners — Example 153
#[derive(Debug)]
struct Pair<K, V> {
    key: K,
    value: V,
}

fn main() {
    let a = Pair { key: "age", value: 34 };
    let b = Pair { key: 7, value: String::from("seven") };
    let c = Pair { key: 'x', value: true };
    println!("{a:?}\n{b:?}\n{c:?}");
}
