mod items;
mod library;

use items::{Book, Film, Magazine};
use library::{Library, money};

fn book(
    code: &str,
    title: &str,
    author: &str,
    pages: u32,
) -> Box<Book> {
    Box::new(Book {
        code: code.into(),
        title: title.into(),
        author: author.into(),
        pages,
    })
}

fn main() {
    let mut lib = Library::new();
    let catalog: Vec<Box<dyn items::Item>> = vec![
        book("B1", "The Rust Way", "A. Lovelace", 320),
        book("B2", "Gardens of Rust", "T. Oak", 210),
        Box::new(Film {
            code: "F1".into(),
            title: "Iron Crab".into(),
            minutes: 112,
        }),
        Box::new(Magazine {
            code: "M1".into(),
            title: "Systems Monthly".into(),
            issue: 42,
        }),
    ];
    for item in catalog {
        lib.add_item(item).expect("unique codes");
    }

    let ana = lib.add_member("Ana");
    let leo = lib.add_member("Leo");

    // Each action prints its result or the error
    let act = |lib: &mut Library,
               label: &str,
               r: Result<
        String,
        library::LibraryError,
    >| {
        match r {
            Ok(msg) => println!(
                "day {:>2}  {label}: {msg}",
                lib.today
            ),
            Err(e) => println!(
                "day {:>2}  {label}: ERROR {e}",
                lib.today
            ),
        }
    };

    let r = lib
        .borrow(ana, "B1")
        .map(|d| format!("due day {d}"));
    act(&mut lib, "Ana borrows B1", r);
    let r = lib
        .borrow(ana, "F1")
        .map(|d| format!("due day {d}"));
    act(&mut lib, "Ana borrows F1", r);
    let r = lib
        .borrow(leo, "M1")
        .map(|d| format!("due day {d}"));
    act(&mut lib, "Leo borrows M1", r);
    let r = lib
        .borrow(leo, "B1")
        .map(|d| format!("due day {d}"));
    act(&mut lib, "Leo borrows B1", r);

    lib.today = 15; // a week passes...
    let r = lib
        .give_back("F1")
        .map(|f| format!("fee {}", money(f)));
    act(&mut lib, "F1 returned", r);
    let r = lib
        .borrow(ana, "B2")
        .map(|d| format!("due day {d}"));
    act(&mut lib, "Ana borrows B2", r);

    lib.today = 30;
    for loan in lib.overdue() {
        println!(
            "overdue: {} (due day {})",
            loan.item_code, loan.due_day
        );
    }
    let r = lib
        .pay(ana, 700)
        .map(|d| format!("debt {}", money(d)));
    act(&mut lib, "Ana pays", r);
    let r = lib
        .borrow(ana, "B2")
        .map(|d| format!("due day {d}"));
    act(&mut lib, "Ana borrows B2", r);
    let owes = lib
        .member(leo)
        .map(|m| m.debt_cents)
        .unwrap_or(0);
    println!("Leo owes {}", money(owes));

    println!("\nSearch 'rust':");
    for item in lib.search("rust") {
        println!("  {}", item.describe());
    }
    println!("\n{}", lib.report());
}
