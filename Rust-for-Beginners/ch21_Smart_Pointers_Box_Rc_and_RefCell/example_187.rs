// Book: Rust for Beginners — Example 187
#[derive(Debug)]
enum List {
    Node(i32, Box<List>),
    Empty,
}

use List::{Empty, Node};

fn sum(list: &List) -> i32 {
    match list {
        Node(value, rest) => value + sum(rest),
        Empty => 0,
    }
}

fn main() {
    let list = Node(
        1,
        Box::new(Node(
            2,
            Box::new(Node(3, Box::new(Empty))),
        )),
    );
    println!("{list:?}");
    println!("sum = {}", sum(&list));
}
