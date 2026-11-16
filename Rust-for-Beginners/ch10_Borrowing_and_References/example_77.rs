// Book: Rust for Beginners — Example 77
fn main() {
    let mut list = String::from("apples");

    let r1 = &list;
    let r2 = &list;
    println!("Reading: {r1} and {r2}");
    // r1 and r2 are not used after this point,
    // so their borrows end here.

    let r3 = &mut list; // OK: no active shared borrows
    r3.push_str(", pears");
    println!("After writing: {r3}");
}
