// Book: Rust for Beginners — Example 07
fn main() {
    let scores = [72, 45, 90, 38, 66, 81];
    let pass_mark = 50;

    let mut total = 0; // accumulator
    let mut passed = 0; // counter

    for s in scores {
        total += s;
        if s >= pass_mark {
            passed += 1;
        }
    }

    println!("Total points: {total}");
    println!("Students who passed: {passed}");
}
