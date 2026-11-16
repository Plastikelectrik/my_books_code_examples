// Book: Rust for Beginners — Example 28
fn main() {
    let mut score = 0;
    score += 50; // collected a coin
    score += 120; // defeated an enemy
    score -= 30; // took damage
    score *= 2; // double-points bonus
    println!("Final score: {score}");
}
