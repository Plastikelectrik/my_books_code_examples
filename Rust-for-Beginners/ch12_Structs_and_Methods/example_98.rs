// Book: Rust for Beginners — Example 98
struct User {
    username: String,
    email: String,
    active: bool,
}

fn new_user(username: String, email: String) -> User {
    User {
        username, // same as username: username
        email,    // same as email: email
        active: true,
    }
}

fn main() {
    let u = new_user(
        String::from("ferris"),
        String::from("ferris@example.com"),
    );
    println!("{} <{}>", u.username, u.email);
    println!("active={}", u.active);
}
