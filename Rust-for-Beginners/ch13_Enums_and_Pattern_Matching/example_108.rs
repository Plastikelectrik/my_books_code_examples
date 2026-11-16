// Book: Rust for Beginners — Example 108
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

fn action(light: &TrafficLight) -> &str {
    match light {
        TrafficLight::Red => "Stop",
        TrafficLight::Yellow => "Prepare to stop",
        TrafficLight::Green => "Go",
    }
}

fn main() {
    let lights = [
        TrafficLight::Green,
        TrafficLight::Yellow,
        TrafficLight::Red,
    ];
    for l in &lights {
        println!("{}", action(l));
    }
}
