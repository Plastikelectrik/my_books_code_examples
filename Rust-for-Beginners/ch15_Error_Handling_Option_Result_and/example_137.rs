// Book: Rust for Beginners — Example 137
use std::fs;
use std::io;

fn save_and_load() -> io::Result<String> {
    fs::write("notes.txt", "Buy milk\nCall mom\n")?;
    let content = fs::read_to_string("notes.txt")?;
    Ok(content)
}

fn main() {
    match save_and_load() {
        Ok(text) => {
            for (i, line) in text.lines().enumerate() {
                println!("{}. {line}", i + 1);
            }
        }
        Err(e) => println!("File problem: {e}"),
    }

    match fs::read_to_string("missing.txt") {
        Ok(_) => println!("found it"),
        Err(e) => {
            println!("Could not read missing.txt: {e}")
        }
    }
}
