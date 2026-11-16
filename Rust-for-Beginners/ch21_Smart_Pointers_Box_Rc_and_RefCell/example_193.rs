// Book: Rust for Beginners — Example 193
use std::cell::RefCell;
use std::rc::{Rc, Weak};

struct Folder {
    name: String,
    parent: RefCell<Weak<Folder>>,
    children: RefCell<Vec<Rc<Folder>>>,
}

fn new_folder(name: &str) -> Rc<Folder> {
    Rc::new(Folder {
        name: name.to_string(),
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(Vec::new()),
    })
}

fn add_child(parent: &Rc<Folder>, child: Rc<Folder>) {
    *child.parent.borrow_mut() = Rc::downgrade(parent);
    parent.children.borrow_mut().push(child);
}

fn path(folder: &Folder) -> String {
    match folder.parent.borrow().upgrade() {
        Some(p) => {
            format!("{}/{}", path(&p), folder.name)
        }
        None => folder.name.clone(),
    }
}

fn main() {
    let home = new_folder("home");
    let docs = new_folder("docs");
    let rust = new_folder("rust");
    add_child(&home, Rc::clone(&docs));
    add_child(&docs, Rc::clone(&rust));

    println!("{}", path(&rust));
    println!(
        "home has {} child",
        home.children.borrow().len()
    );
}
