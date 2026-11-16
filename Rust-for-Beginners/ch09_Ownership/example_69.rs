// Book: Rust for Beginners — Example 69
fn main() {
    let name = String::from("Rustacean");
    let age = 7;

    greet(name); // name is MOVED into greet
    show_age(age); // age is COPIED into show_age

    // println!("{name}"); // error: name was moved
    println!("age is still usable: {age}");
}

fn greet(person: String) {
    println!("Hello, {person}!");
} // person goes out of scope: the String is dropped

fn show_age(years: i32) {
    println!("Age: {years}");
}
