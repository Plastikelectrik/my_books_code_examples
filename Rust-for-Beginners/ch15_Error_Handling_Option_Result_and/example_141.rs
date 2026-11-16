// Book: Rust for Beginners — Example 141
#[derive(Debug)]
struct Line {
    name: String,
    qty: u32,
    price_cents: u32,
}

fn parse_line(raw: &str) -> Result<Line, String> {
    let parts: Vec<&str> =
        raw.split(',').map(|p| p.trim()).collect();
    if parts.len() != 3 {
        return Err(format!(
            "expected 3 fields, got {}",
            parts.len()
        ));
    }
    let name = parts[0];
    if name.is_empty() {
        return Err("empty name".to_string());
    }
    let qty: u32 = parts[1].parse().map_err(|_| {
        format!("bad quantity '{}'", parts[1])
    })?;
    let price_cents: u32 =
        parts[2].parse().map_err(|_| {
            format!("bad price '{}'", parts[2])
        })?;
    Ok(Line { name: name.to_string(), qty, price_cents })
}

fn main() {
    let input = "pen, 3, 150\nbook,1,1299\n,2,100\n\
                 lamp,two,2500\nmug,2\ncup,4,350";

    let mut total = 0;
    for (n, raw) in input.lines().enumerate() {
        match parse_line(raw) {
            Ok(line) => {
                total += line.qty * line.price_cents;
                println!(
                    "line {}: ok {:?}",
                    n + 1,
                    line.name
                );
            }
            Err(e) => {
                println!("line {}: skipped ({e})", n + 1)
            }
        }
    }
    println!(
        "Total: {}.{:02} EUR",
        total / 100,
        total % 100
    );
}
