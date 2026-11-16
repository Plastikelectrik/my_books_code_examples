// Book: Rust for Beginners — Example 24
const DAILY_GOAL: u32 = 8_000;

fn main() {
    let owner = ("Marco", 'M');
    let steps: [u32; 7] = [
        7_500, 9_200, 8_100, 6_400, 10_300, 12_000, 5_900,
    ];

    let mut total: u32 = 0;
    let mut days_on_goal: u8 = 0;

    for s in steps {
        total += s;
        if s >= DAILY_GOAL {
            days_on_goal += 1;
        }
    }

    let average = total as f64 / steps.len() as f64;
    let goal_reached = days_on_goal >= 4;

    println!("Report for {} ({})", owner.0, owner.1);
    println!("Total steps: {total}");
    println!("Daily average: {average:.1}");
    println!("Days on goal: {days_on_goal} of 7");
    println!("Weekly target met: {goal_reached}");
}
