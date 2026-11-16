// Book: Rust for Beginners — Example 97
struct Counter {
    label: String,
    value: u32,
}

fn main() {
    let mut visits = Counter {
        label: String::from("Page visits"),
        value: 0,
    };

    visits.value += 1;
    visits.value += 1;
    visits.label.push_str(" (today)");

    println!("{}: {}", visits.label, visits.value);
}
