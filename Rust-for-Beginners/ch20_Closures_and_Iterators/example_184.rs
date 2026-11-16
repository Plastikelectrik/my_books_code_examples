// Book: Rust for Beginners — Example 184
struct Fibonacci {
    current: u64,
    next: u64,
}

impl Fibonacci {
    fn new() -> Self {
        Fibonacci { current: 0, next: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<u64> {
        let value = self.current;
        self.current = self.next;
        self.next = value + self.next;
        Some(value) // this iterator never ends
    }
}

fn main() {
    let first_ten: Vec<u64> =
        Fibonacci::new().take(10).collect();
    println!("{first_ten:?}");

    let even_sum: u64 = Fibonacci::new()
        .take_while(|&n| n < 1_000)
        .filter(|n| n % 2 == 0)
        .sum();
    println!("sum of even values below 1000: {even_sum}");
}
