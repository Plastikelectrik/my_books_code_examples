// Book: Rust for Beginners — Example 38
fn main() {
    let is_member = true;
    let total = 80.0;

    if is_member {
        if total >= 50.0 {
            println!("Member discount: 15%");
        } else {
            println!("Member discount: 5%");
        }
    } else {
        println!("No discount. Join our club!");
    }
}
