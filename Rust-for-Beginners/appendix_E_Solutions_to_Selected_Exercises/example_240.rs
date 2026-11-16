// Book: Rust for Beginners — Example 240
fn main() {
    let total = 3725;
    let hours = total / 3600;
    let minutes = (total % 3600) / 60;
    let seconds = total % 60;
    println!(
        "{total} s = {hours}h {minutes}m {seconds}s"
    );
}
