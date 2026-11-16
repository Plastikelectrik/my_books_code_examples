// Book: Rust for Beginners — Example 111
fn find_index(
    names: &[&str],
    target: &str,
) -> Option<usize> {
    for (i, name) in names.iter().enumerate() {
        if *name == target {
            return Some(i);
        }
    }
    None
}

fn main() {
    let team = ["Alice", "Bruno", "Chen"];

    for who in ["Chen", "Dana"] {
        match find_index(&team, who) {
            Some(i) => println!("{who} is at {i}"),
            None => println!("{who} is not in the team"),
        }
    }
}
