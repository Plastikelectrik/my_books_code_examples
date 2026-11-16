// Book: Rust for Beginners — Example 60
fn main() {
    let names = ["Ana", "Bruno", "Clara", "David"];
    let scores = [88, 54, 71, 39];

    print_header();
    for i in 0..names.len() {
        print_line(names[i], scores[i]);
    }
    println!("Class average: {:.1}", average(scores));
}

fn print_header() {
    let (n, s, r) = ("Name", "Score", "Result");
    println!("{n:<8} {s:>5}  {r}");
    println!("{}", "-".repeat(24));
}

fn print_line(name: &str, score: u32) {
    let result =
        if passed(score) { "PASS" } else { "FAIL" };
    println!("{name:<8} {score:>5}  {result}");
}

fn passed(score: u32) -> bool {
    score >= 50
}

fn average(scores: [u32; 4]) -> f64 {
    let mut sum = 0;
    for s in scores {
        sum += s;
    }
    sum as f64 / scores.len() as f64
}
