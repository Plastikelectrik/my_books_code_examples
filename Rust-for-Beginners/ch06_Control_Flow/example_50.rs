// Book: Rust for Beginners — Example 50
fn main() {
    let limit = 30;
    let mut prime_count = 0;

    for n in 2..=limit {
        let mut is_prime = true;
        let mut d = 2;

        while d * d <= n {
            if n % d == 0 {
                is_prime = false;
                break;
            }
            d += 1;
        }

        if is_prime {
            print!("{n} ");
            prime_count += 1;
        }
    }

    println!();
    println!("{prime_count} primes up to {limit}.");
}
