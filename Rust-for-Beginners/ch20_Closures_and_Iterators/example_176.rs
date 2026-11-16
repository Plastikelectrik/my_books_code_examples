// Book: Rust for Beginners — Example 176
fn make_multiplier(factor: i32) -> impl Fn(i32) -> i32 {
    move |x| x * factor // the closure owns factor
}

fn make_greeter(name: String) -> impl Fn() -> String {
    move || format!("Hi, {name}!")
}

fn main() {
    let triple = make_multiplier(3);
    let tenfold = make_multiplier(10);
    let hi_ana = make_greeter(String::from("Ana"));

    println!("{} {}", triple(7), tenfold(7));
    println!("{}", hi_ana());
}
