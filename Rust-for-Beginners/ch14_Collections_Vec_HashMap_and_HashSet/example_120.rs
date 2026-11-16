// Book: Rust for Beginners — Example 120
fn main() {
    let mut v = vec![10, 20, 30];

    v.push(40); // add at the end
    v.insert(0, 5); // insert at position 0
    v[2] = 99; // replace position 2
    println!("after changes: {v:?}");

    let last = v.pop(); // remove from the end
    let removed = v.remove(1); // remove position 1
    println!("popped {last:?}, removed {removed}");
    println!("now: {v:?}");

    v.extend([1, 2, 3]); // add several values
    v.sort(); // sort in place
    v.dedup(); // remove consecutive duplicates
    println!("sorted: {v:?}");

    v.retain(|x| *x > 2); // keep only values > 2
    println!("retained: {v:?}");
    println!("contains 99? {}", v.contains(&99));

    v.clear();
    println!("empty? {}", v.is_empty());
}
