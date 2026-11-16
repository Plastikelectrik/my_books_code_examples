// Book: Rust for Beginners — Example 56
fn main() {
    println!("main: start");
    let result = level_one(3);
    println!("main: got {result}");
}

fn level_one(x: i32) -> i32 {
    println!("  level_one: x = {x}");
    let y = level_two(x * 2);
    println!("  level_one: returning {}", y + 1);
    y + 1
}

fn level_two(z: i32) -> i32 {
    println!("    level_two: z = {z}");
    z * 10
}
