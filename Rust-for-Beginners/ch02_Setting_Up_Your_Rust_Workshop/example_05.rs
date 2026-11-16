// Book: Rust for Beginners — Example 05
fn main() {
    let apples = 3;
    let pears = 5;

    // Variable name inside the braces
    println!("I have {apples} apples.");

    // Empty braces, values after the text
    println!(
        "I have {} apples and {} pears.",
        apples, pears
    );

    // Expressions must go after the text
    println!("That is {} fruits.", apples + pears);
}
