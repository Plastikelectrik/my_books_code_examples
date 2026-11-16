// Book: Rust for Beginners — Example 128
use std::collections::HashSet;

fn main() {
    let alice: HashSet<&str> =
        ["rust", "python", "sql"].into_iter().collect();
    let bob: HashSet<&str> =
        ["rust", "go", "sql", "java"]
            .into_iter()
            .collect();

    let mut both: Vec<_> =
        alice.intersection(&bob).collect();
    let mut either: Vec<_> = alice.union(&bob).collect();
    let mut only_alice: Vec<_> =
        alice.difference(&bob).collect();
    both.sort();
    either.sort();
    only_alice.sort();

    println!("both know:   {both:?}");
    println!("either knows: {either:?}");
    println!("only Alice:  {only_alice:?}");
}
