// Book: Rust for Beginners — Example 214
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("{} argument(s)", args.len());
    for (i, a) in args.iter().enumerate() {
        println!("  args[{i}] = {a}");
    }
}
