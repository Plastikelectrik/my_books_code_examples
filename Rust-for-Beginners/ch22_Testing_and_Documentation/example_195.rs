// Book: Rust for Beginners — Example 195
fn is_valid_username(name: &str) -> bool {
    let len = name.chars().count();
    (3..=16).contains(&len)
        && name.chars().all(|c| {
            c.is_ascii_alphanumeric() || c == '_'
        })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn accepts_normal_names() {
        for name in ["ana", "rust_fan", "Player01"] {
            assert!(
                is_valid_username(name),
                "'{name}' should be valid"
            );
        }
    }

    #[test]
    fn rejects_bad_names() {
        for name in
            ["ab", "has space", "way_too_long_username"]
        {
            assert!(
                !is_valid_username(name),
                "'{name}' should be invalid"
            );
        }
    }
}

fn main() {
    println!("{}", is_valid_username("ferris"));
}
