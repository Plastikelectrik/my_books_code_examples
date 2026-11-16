// Book: Rust for Beginners — Example 13
const SECONDS_PER_MINUTE: u32 = 60;
const MINUTES_PER_HOUR: u32 = 60;
const SECONDS_PER_HOUR: u32 =
    SECONDS_PER_MINUTE * MINUTES_PER_HOUR;

fn main() {
    let hours = 3;
    let seconds = hours * SECONDS_PER_HOUR;
    println!("{hours} hours = {seconds} seconds");
}
