// Book: Rust for Beginners — Example 192
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Account {
    owner: String,
    balance: i64,
}

fn main() {
    let shared = Rc::new(RefCell::new(Account {
        owner: "Family".into(),
        balance: 1000,
    }));

    // Two family members share the same account
    let mom = Rc::clone(&shared);
    let son = Rc::clone(&shared);

    mom.borrow_mut().balance -= 200; // groceries
    son.borrow_mut().balance -= 50; // cinema

    let acc = shared.borrow();
    println!("{}: {} EUR", acc.owner, acc.balance);
    println!("owners: {}", Rc::strong_count(&shared));
}
