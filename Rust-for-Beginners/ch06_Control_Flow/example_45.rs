// Book: Rust for Beginners — Example 45
fn main() {
    let readings = [12, -1, 15, 18, -1, 999, 20];
    let mut sum = 0;

    for r in readings {
        if r == -1 {
            continue; // invalid reading: skip it
        }
        if r == 999 {
            break; // end-of-data marker: stop
        }
        sum += r;
    }

    println!("Sum of valid readings: {sum}");
}
