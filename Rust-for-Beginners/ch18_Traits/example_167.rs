// Book: Rust for Beginners — Example 167
trait Notifier {
    fn channel(&self) -> &str;
    fn send(&self, message: &str) -> bool;

    fn send_all(&self, messages: &[&str]) -> usize {
        let mut sent = 0;
        for m in messages {
            if self.send(m) {
                sent += 1;
            }
        }
        sent
    }
}

struct EmailNotifier {
    address: String,
}
struct SmsNotifier {
    phone: String,
    max_len: usize,
}

impl Notifier for EmailNotifier {
    fn channel(&self) -> &str {
        "email"
    }
    fn send(&self, message: &str) -> bool {
        println!(
            "  [email to {}] {message}",
            self.address
        );
        true
    }
}

impl Notifier for SmsNotifier {
    fn channel(&self) -> &str {
        "sms"
    }
    fn send(&self, message: &str) -> bool {
        if message.len() > self.max_len {
            println!("  [sms] too long, not sent");
            return false;
        }
        println!("  [sms to {}] {message}", self.phone);
        true
    }
}

fn report(n: &impl Notifier, sent: usize, total: usize) {
    println!("{}: {sent}/{total} sent", n.channel());
}

fn main() {
    let notifiers: Vec<Box<dyn Notifier>> = vec![
        Box::new(EmailNotifier {
            address: "a@b.com".into(),
        }),
        Box::new(SmsNotifier {
            phone: "+34 600 000 000".into(),
            max_len: 20,
        }),
    ];

    let msgs =
        ["Server is up", "Disk usage at 91 percent"];
    for n in &notifiers {
        println!("Using {}:", n.channel());
        let sent = n.send_all(&msgs);
        println!(
            "{}: {sent}/{} sent",
            n.channel(),
            msgs.len()
        );
    }

    let email =
        EmailNotifier { address: "ops@b.com".into() };
    let sent = email.send_all(&["Backup done"]);
    report(&email, sent, 1);
}
