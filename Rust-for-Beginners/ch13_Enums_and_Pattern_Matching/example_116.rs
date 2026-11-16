// Book: Rust for Beginners — Example 116
#[derive(Debug)]
enum Event {
    KeyPress(char),
    Click { x: i32, y: i32 },
    Scroll(i32),
    Quit,
}

fn handle(e: &Event) -> String {
    match e {
        Event::KeyPress('q') | Event::Quit => {
            "quit".into()
        }
        Event::KeyPress(c @ '0'..='9') => {
            format!("digit {c}")
        }
        Event::KeyPress(c) => format!("key {c}"),
        Event::Click { x: 0, y: 0 } => "origin".into(),
        Event::Click { x, y } if *x < 0 || *y < 0 => {
            "click outside window".into()
        }
        Event::Click { x, y } => format!("at {x},{y}"),
        Event::Scroll(n) if *n > 0 => format!("down {n}"),
        Event::Scroll(n) => format!("up {}", -n),
    }
}

fn main() {
    let events = [
        Event::KeyPress('7'),
        Event::KeyPress('a'),
        Event::Click { x: 0, y: 0 },
        Event::Click { x: -5, y: 20 },
        Event::Click { x: 30, y: 40 },
        Event::Scroll(3),
        Event::Scroll(-2),
        Event::KeyPress('q'),
    ];
    for e in &events {
        println!("{e:?} -> {}", handle(e));
    }
}
