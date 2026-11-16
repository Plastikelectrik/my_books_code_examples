// Book: Rust for Beginners — Example 73
fn main() {
    let item = String::from("keyboard");
    let quantity = 3;

    // item moves into register; quantity is copied
    let record = register(item, quantity);
    // println!("{item}"); // error: item was moved

    println!("Record: {record}");
    println!("Quantity still usable: {quantity}");

    let backup = record.clone(); // explicit deep copy
    archive(record); // record moves into archive
    // println!("{record}"); // error: record was moved

    println!("Backup: {backup}");
}

fn register(name: String, qty: i32) -> String {
    format!("{qty} x {name}")
}

fn archive(entry: String) {
    println!("Archived: {entry}");
} // entry is dropped here
