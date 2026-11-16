// Book: Rust for Beginners — Example 126
use std::collections::HashMap;

fn main() {
    let name = String::from("Rosa");
    let role = String::from("admin");

    let mut roles = HashMap::new();
    roles.insert(name, role);
    // name and role were moved into the map

    // Look up with a &str: no need to build a String
    if let Some(r) = roles.get("Rosa") {
        println!("Rosa is {r}");
    }
}
