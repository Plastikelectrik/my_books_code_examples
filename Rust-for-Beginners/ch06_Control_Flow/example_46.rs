// Book: Rust for Beginners — Example 46
fn main() {
    let grid = [[1, 3, 5], [7, 8, 9], [11, 13, 15]];

    'search: for row in grid {
        for value in row {
            if value % 2 == 0 {
                println!("First even number: {value}");
                break 'search; // exit both loops
            }
        }
    }
}
