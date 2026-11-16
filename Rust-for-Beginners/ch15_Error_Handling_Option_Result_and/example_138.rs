// Book: Rust for Beginners — Example 138
use std::fs;
use std::io::ErrorKind;

fn read_config() -> String {
    match fs::read_to_string("config.txt") {
        Ok(text) => text,
        Err(e) if e.kind() == ErrorKind::NotFound => {
            println!(
                "No config file, creating a default one"
            );
            let default = String::from("theme=light\n");
            fs::write("config.txt", &default)
                .expect("cannot write config.txt");
            default
        }
        Err(e) => panic!("cannot read config.txt: {e}"),
    }
}

fn main() {
    let _ = std::fs::remove_file("config.txt");
    print!("first run: {}", read_config());
    print!("second run: {}", read_config());
}
