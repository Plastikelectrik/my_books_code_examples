// Book: Rust for Beginners — Example 172
#[derive(Debug)]
struct Setting<'a> {
    key: &'a str,
    value: &'a str,
}

fn parse_line(line: &str) -> Option<Setting<'_>> {
    let line = line.trim();
    if line.is_empty() || line.starts_with('#') {
        return None;
    }
    let (key, value) = line.split_once('=')?;
    Some(Setting { key: key.trim(), value: value.trim() })
}

fn get<'a>(
    settings: &[Setting<'a>],
    key: &str,
) -> Option<&'a str> {
    for s in settings {
        if s.key == key {
            return Some(s.value);
        }
    }
    None
}

fn main() {
    let config = String::from(
        "# server settings\nhost = example.com\n\
         port = 8080\n\nmode=production\nbroken line",
    );

    let settings: Vec<Setting> =
        config.lines().filter_map(parse_line).collect();

    for s in &settings {
        println!("{:<5} -> {}", s.key, s.value);
    }
    println!("port is {:?}", get(&settings, "port"));
    println!("user is {:?}", get(&settings, "user"));
}
