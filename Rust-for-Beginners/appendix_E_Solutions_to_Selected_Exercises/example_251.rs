// Book: Rust for Beginners — Example 251
#[derive(Debug, PartialEq)]
enum Command {
    Add(String),
    Remove(u32),
    List,
    Unknown,
}

fn parse_command(input: &str) -> Command {
    let mut parts = input.trim().splitn(2, ' ');
    match (parts.next(), parts.next()) {
        (Some("add"), Some(item)) => {
            Command::Add(item.to_string())
        }
        (Some("remove"), Some(n)) => match n.parse() {
            Ok(n) => Command::Remove(n),
            Err(_) => Command::Unknown,
        },
        (Some("list"), None) => Command::List,
        _ => Command::Unknown,
    }
}

fn main() {
    for s in ["add milk", "remove 3", "list", "dance"] {
        println!("{s:<9} -> {:?}", parse_command(s));
    }
}
