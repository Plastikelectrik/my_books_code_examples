// Book: Rust for Beginners — Example 48
fn main() {
    let temperature = 31;

    let advice = match temperature {
        i32::MIN..=0 => "Freezing: stay inside",
        1..=15 => "Cold: wear a coat",
        16..=25 => "Pleasant: enjoy the day",
        t if t > 40 => "Extreme heat: be careful",
        _ => "Hot: drink plenty of water",
    };

    println!("{temperature} degrees. {advice}.");
}
