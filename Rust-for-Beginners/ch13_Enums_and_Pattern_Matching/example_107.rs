// Book: Rust for Beginners — Example 107
#[derive(Debug)]
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

fn main() {
    let light = TrafficLight::Red;
    let next = TrafficLight::Green;
    println!("{light:?} then {next:?}");
}
