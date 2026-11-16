// Book: Rust for Beginners — Example 140
use std::fs;

fn read_number(path: &str) -> Result<i64, String> {
    let text = fs::read_to_string(path).map_err(|e| {
        format!("cannot read {path}: {e}")
    })?;
    let n = text.trim().parse::<i64>().map_err(|e| {
        format!("bad number in {path}: {e}")
    })?;
    Ok(n)
}

fn main() {
    fs::write("good.txt", "1234\n").unwrap();
    fs::write("bad.txt", "12a4\n").unwrap();

    for file in ["good.txt", "bad.txt"] {
        match read_number(file) {
            Ok(n) => println!("{file}: {n}"),
            Err(e) => println!("{e}"),
        }
    }
}
