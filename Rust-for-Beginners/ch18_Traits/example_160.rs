// Book: Rust for Beginners — Example 160
trait Summary {
    fn summarize(&self) -> String;
}

struct Email {
    subject: String,
}
struct Invoice {
    number: u32,
    total: f64,
}

impl Summary for Email {
    fn summarize(&self) -> String {
        format!("Email: {}", self.subject)
    }
}
impl Summary for Invoice {
    fn summarize(&self) -> String {
        format!(
            "Invoice #{}: {:.2}",
            self.number, self.total
        )
    }
}

// Short form: impl Trait
fn notify(item: &impl Summary) {
    println!("New item! {}", item.summarize());
}

// Long form: a generic with a trait bound
fn archive<T: Summary>(item: &T) {
    println!("Archived: {}", item.summarize());
}

fn main() {
    let e = Email { subject: "Meeting at 10".into() };
    let i = Invoice { number: 42, total: 99.5 };
    notify(&e);
    notify(&i);
    archive(&i);
}
