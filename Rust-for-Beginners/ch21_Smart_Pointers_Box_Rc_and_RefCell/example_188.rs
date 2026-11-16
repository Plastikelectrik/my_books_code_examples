// Book: Rust for Beginners — Example 188
#[derive(Debug)]
struct Tree {
    root: Option<Box<Node>>,
}

#[derive(Debug)]
struct Node {
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Tree {
    fn new() -> Self {
        Tree { root: None }
    }

    fn insert(&mut self, value: i32) {
        let mut slot = &mut self.root;
        while let Some(node) = slot {
            slot = if value < node.value {
                &mut node.left
            } else {
                &mut node.right
            };
        }
        *slot = Some(Box::new(Node {
            value,
            left: None,
            right: None,
        }));
    }

    fn contains(&self, value: i32) -> bool {
        let mut current = &self.root;
        while let Some(node) = current {
            if value == node.value {
                return true;
            }
            current = if value < node.value {
                &node.left
            } else {
                &node.right
            };
        }
        false
    }

    fn in_order(&self) -> Vec<i32> {
        fn walk(
            node: &Option<Box<Node>>,
            out: &mut Vec<i32>,
        ) {
            if let Some(n) = node {
                walk(&n.left, out);
                out.push(n.value);
                walk(&n.right, out);
            }
        }
        let mut out = Vec::new();
        walk(&self.root, &mut out);
        out
    }
}

fn main() {
    let mut t = Tree::new();
    for v in [50, 30, 70, 20, 40, 60, 80] {
        t.insert(v);
    }
    println!("sorted: {:?}", t.in_order());
    println!("contains 60? {}", t.contains(60));
    println!("contains 65? {}", t.contains(65));
}
