// Book: Rust for Beginners — Example 21
fn main() {
    let person = ("Lucia", 31, 1.68);

    // Access by position, starting at 0
    println!("Name: {}", person.0);
    println!("Age: {}", person.1);
    println!("Height: {} m", person.2);

    // Destructuring: unpack into variables
    let (name, age, height) = person;
    println!("{name} is {age} and {height} m tall");
}
