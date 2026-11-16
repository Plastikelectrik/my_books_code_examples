// Book: Rust for Beginners — Example 177
fn apply_twice<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(f(x))
}

fn repeat<F: FnMut()>(times: u32, mut action: F) {
    for _ in 0..times {
        action();
    }
}

fn run_once<F: FnOnce() -> String>(f: F) -> String {
    f()
}

fn main() {
    println!("{}", apply_twice(|n| n + 10, 1));

    let mut log = Vec::new();
    repeat(3, || log.push("tick"));
    println!("{log:?}");

    let message = String::from("consumed!");
    let result = run_once(move || message); // moved
    println!("{result}");
}
