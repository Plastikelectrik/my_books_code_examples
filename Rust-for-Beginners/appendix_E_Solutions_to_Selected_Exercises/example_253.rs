// Book: Rust for Beginners — Example 253
fn parse_point(text: &str) -> Result<(i32, i32), String> {
    let (a, b) = text
        .split_once(',')
        .ok_or(format!("missing comma in '{text}'"))?;
    let x = a
        .trim()
        .parse()
        .map_err(|_| format!("bad x: {a}"))?;
    let y = b
        .trim()
        .parse()
        .map_err(|_| format!("bad y: {b}"))?;
    Ok((x, y))
}

fn main() {
    println!("{:?}", parse_point("3,-4"));
    println!("{:?}", parse_point("3;4"));
    println!("{:?}", parse_point("a,4"));
}
