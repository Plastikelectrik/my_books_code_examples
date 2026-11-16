// Book: Rust for Beginners — Example 132
fn parse_age(text: &str) -> Result<u8, String> {
    let age: i32 = match text.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            return Err(format!(
                "'{text}' is not a number"
            ));
        }
    };
    if age < 0 || age > 130 {
        return Err(format!(
            "{age} is not a realistic age"
        ));
    }
    Ok(age as u8)
}

fn main() {
    for input in ["34", " 7 ", "abc", "200"] {
        match parse_age(input) {
            Ok(age) => println!("valid age: {age}"),
            Err(msg) => println!("invalid: {msg}"),
        }
    }
}
