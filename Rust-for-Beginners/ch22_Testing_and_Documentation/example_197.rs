// Book: Rust for Beginners — Example 197
fn parse_price(text: &str) -> Result<u32, String> {
    let (euros, cents) = text
        .split_once('.')
        .ok_or(format!("missing '.' in {text}"))?;
    let e: u32 = euros
        .parse()
        .map_err(|_| "bad euros".to_string())?;
    let c: u32 = cents
        .parse()
        .map_err(|_| "bad cents".to_string())?;
    if cents.len() != 2 {
        return Err("cents need two digits".into());
    }
    Ok(e * 100 + c)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_valid_price() -> Result<(), String> {
        assert_eq!(parse_price("12.50")?, 1250);
        assert_eq!(parse_price("0.07")?, 7);
        Ok(())
    }

    #[test]
    fn reports_errors() {
        assert!(parse_price("12").is_err());
        assert!(parse_price("x.10").is_err());
        assert!(parse_price("3.5").is_err());
    }
}
