// Book: Rust for Beginners — Example 182
fn main() {
    let temps =
        [18.5, 22.1, 25.3, 19.8, 30.2, 27.4, 21.0];

    let count = temps.iter().count();
    let total: f64 = temps.iter().sum();
    let hot_days =
        temps.iter().filter(|t| **t > 25.0).count();
    let any_freezing = temps.iter().any(|t| *t < 0.0);
    let all_mild = temps.iter().all(|t| *t > 15.0);
    let first_hot = temps.iter().position(|t| *t > 25.0);
    let max =
        temps.iter().cloned().fold(f64::MIN, f64::max);

    println!(
        "days: {count}, average: {:.1}",
        total / 7.0
    );
    println!("hot days: {hot_days}");
    println!("any freezing? {any_freezing}");
    println!("all mild? {all_mild}");
    println!("first hot day: {first_hot:?}");
    println!("max: {max}");
}
