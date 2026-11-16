use crate::items::{Book, Film, Magazine};
use crate::library::*;

fn sample() -> (Library, u32) {
    let mut lib = Library::new();
    lib.add_item(Box::new(Book {
        code: "B1".into(),
        title: "Book One".into(),
        author: "X".into(),
        pages: 10,
    }))
    .unwrap();
    lib.add_item(Box::new(Film {
        code: "F1".into(),
        title: "Film One".into(),
        minutes: 90,
    }))
    .unwrap();
    lib.add_item(Box::new(Magazine {
        code: "M1".into(),
        title: "Mag".into(),
        issue: 1,
    }))
    .unwrap();
    let id = lib.add_member("Test");
    (lib, id)
}

#[test]
fn borrow_sets_due_day_by_kind() {
    let (mut lib, id) = sample();
    assert_eq!(lib.borrow(id, "B1"), Ok(22));
    assert_eq!(lib.borrow(id, "F1"), Ok(8));
}

#[test]
fn magazines_cannot_be_borrowed() {
    let (mut lib, id) = sample();
    assert_eq!(
        lib.borrow(id, "M1"),
        Err(LibraryError::NotLendable("M1".into()))
    );
}

#[test]
fn late_return_charges_fee_and_blocks() {
    let (mut lib, id) = sample();
    lib.borrow(id, "F1").unwrap(); // due day 8
    lib.today = 14; // 6 days late
    assert_eq!(lib.give_back("F1"), Ok(600));
    assert_eq!(lib.member(id).unwrap().debt_cents, 600);
    assert!(matches!(
        lib.borrow(id, "B1"),
        Err(LibraryError::DebtTooHigh { .. })
    ));
    lib.pay(id, 600).unwrap();
    assert!(lib.borrow(id, "B1").is_ok());
}

#[test]
fn early_return_is_free() {
    let (mut lib, id) = sample();
    lib.borrow(id, "B1").unwrap();
    lib.today = 5;
    assert_eq!(lib.give_back("B1"), Ok(0));
}

#[test]
fn duplicate_codes_are_rejected() {
    let (mut lib, _) = sample();
    let again = Box::new(Magazine {
        code: "M1".into(),
        title: "Other".into(),
        issue: 2,
    });
    assert_eq!(
        lib.add_item(again),
        Err(LibraryError::DuplicateCode("M1".into()))
    );
}
