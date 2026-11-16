// Book: Rust for Beginners — Example 99
struct Settings {
    volume: u8,
    brightness: u8,
    dark_mode: bool,
    language: String,
}

fn main() {
    let default = Settings {
        volume: 50,
        brightness: 70,
        dark_mode: false,
        language: String::from("en"),
    };

    let night = Settings {
        brightness: 20,
        dark_mode: true,
        ..default
    };

    println!(
        "night: vol {}, bright {}, dark {}, lang {}",
        night.volume,
        night.brightness,
        night.dark_mode,
        night.language
    );
}
