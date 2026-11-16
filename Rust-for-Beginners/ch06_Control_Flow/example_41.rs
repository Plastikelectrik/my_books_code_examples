// Book: Rust for Beginners — Example 41
fn main() {
    let mut savings = 1000.0;
    let rate = 0.07; // 7% per year
    let mut years = 0;

    while savings < 2000.0 {
        savings *= 1.0 + rate;
        years += 1;
    }

    println!("Your savings double in {years} years.");
    println!("Final amount: {savings:.2}");
}
