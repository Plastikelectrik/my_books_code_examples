// Book: Rust for Beginners — Example 37
fn main() {
    let score = 78;

    if score >= 90 {
        println!("Grade A: excellent!");
    } else if score >= 75 {
        println!("Grade B: very good");
    } else if score >= 60 {
        println!("Grade C: good");
    } else if score >= 50 {
        println!("Grade D: pass");
    } else {
        println!("Grade F: try again");
    }
}
