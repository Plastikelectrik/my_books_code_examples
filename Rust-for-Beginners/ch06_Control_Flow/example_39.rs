// Book: Rust for Beginners — Example 39
fn main() {
    let mut counter = 5;

    loop {
        println!("{counter}...");
        counter -= 1;

        if counter == 0 {
            break; // exit the loop
        }
    }

    println!("Liftoff!");
}
