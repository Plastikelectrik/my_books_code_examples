// Book: Rust for Beginners — Example 106
#[derive(Debug)]
struct Account {
    owner: String,
    balance_cents: i64,
    history: Vec<String>,
}

impl Account {
    fn new(owner: &str) -> Self {
        Self {
            owner: owner.to_string(),
            balance_cents: 0,
            history: Vec::new(),
        }
    }

    fn deposit(&mut self, cents: i64) {
        self.balance_cents += cents;
        self.history.push(format!("+{cents}"));
    }

    fn withdraw(&mut self, cents: i64) -> bool {
        if cents > self.balance_cents {
            let note = format!("refused -{cents}");
            self.history.push(note);
            return false;
        }
        self.balance_cents -= cents;
        self.history.push(format!("-{cents}"));
        true
    }

    fn balance(&self) -> String {
        let euros = self.balance_cents / 100;
        let cents = self.balance_cents % 100;
        format!("{euros}.{cents:02} EUR")
    }
}

fn main() {
    let mut acc = Account::new("Noah");
    acc.deposit(15_000);
    acc.withdraw(4_250);
    let ok = acc.withdraw(20_000);

    println!("Owner: {}", acc.owner);
    println!("Big withdrawal accepted? {ok}");
    println!("Balance: {}", acc.balance());
    println!("History: {:?}", acc.history);
}
