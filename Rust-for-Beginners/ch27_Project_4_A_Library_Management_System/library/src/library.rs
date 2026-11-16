use crate::items::Item;
use std::collections::HashMap;
use std::fmt;

pub const MAX_LOANS: usize = 3;
pub const MAX_DEBT_CENTS: u32 = 500;

#[derive(Debug, PartialEq)]
pub enum LibraryError {
    UnknownItem(String),
    UnknownMember(u32),
    DuplicateCode(String),
    NotLendable(String),
    AlreadyBorrowed(String),
    NotBorrowed(String),
    TooManyLoans { member: u32 },
    DebtTooHigh { member: u32, cents: u32 },
}

impl fmt::Display for LibraryError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        use LibraryError::*;
        match self {
            UnknownItem(c) => {
                write!(f, "no item with code {c}")
            }
            UnknownMember(id) => {
                write!(f, "no member {id}")
            }
            DuplicateCode(c) => {
                write!(f, "code {c} already used")
            }
            NotLendable(c) => {
                write!(f, "{c} is reference only")
            }
            AlreadyBorrowed(c) => {
                write!(f, "{c} is already out")
            }
            NotBorrowed(c) => {
                write!(f, "{c} is not borrowed")
            }
            TooManyLoans { member } => {
                write!(f, "member {member}: loan limit")
            }
            DebtTooHigh { member, cents } => write!(
                f,
                "member {member} owes {}",
                money(*cents)
            ),
        }
    }
}

/// Formats cents as "12.34 EUR".
pub fn money(cents: u32) -> String {
    format!("{}.{:02} EUR", cents / 100, cents % 100)
}

#[derive(Debug, Clone)]
pub struct Member {
    pub id: u32,
    pub name: String,
    pub debt_cents: u32,
}

#[derive(Debug, Clone, PartialEq)]
pub struct Loan {
    pub item_code: String,
    pub member_id: u32,
    pub due_day: u32,
}

pub struct Library {
    items: HashMap<String, Box<dyn Item>>,
    members: HashMap<u32, Member>,
    loans: Vec<Loan>,
    next_member_id: u32,
    pub today: u32,
}

impl Library {
    pub fn new() -> Self {
        Library {
            items: HashMap::new(),
            members: HashMap::new(),
            loans: Vec::new(),
            next_member_id: 1,
            today: 1,
        }
    }

    pub fn add_item(
        &mut self,
        item: Box<dyn Item>,
    ) -> Result<(), LibraryError> {
        let code = item.code().to_string();
        if self.items.contains_key(&code) {
            return Err(LibraryError::DuplicateCode(
                code,
            ));
        }
        self.items.insert(code, item);
        Ok(())
    }

    pub fn add_member(&mut self, name: &str) -> u32 {
        let id = self.next_member_id;
        self.next_member_id += 1;
        let m = Member {
            id,
            name: name.to_string(),
            debt_cents: 0,
        };
        self.members.insert(id, m);
        id
    }

    pub fn member(&self, id: u32) -> Option<&Member> {
        self.members.get(&id)
    }

    fn loans_of(&self, member_id: u32) -> usize {
        self.loans
            .iter()
            .filter(|l| l.member_id == member_id)
            .count()
    }

    /// Lends an item. Returns the due day.
    pub fn borrow(
        &mut self,
        member_id: u32,
        code: &str,
    ) -> Result<u32, LibraryError> {
        let member = self.members.get(&member_id).ok_or(
            LibraryError::UnknownMember(member_id),
        )?;
        let item =
            self.items.get(code).ok_or_else(|| {
                LibraryError::UnknownItem(code.into())
            })?;

        let days = item.loan_days().ok_or_else(|| {
            LibraryError::NotLendable(code.into())
        })?;
        if self.loans.iter().any(|l| l.item_code == code)
        {
            return Err(LibraryError::AlreadyBorrowed(
                code.into(),
            ));
        }
        if member.debt_cents > MAX_DEBT_CENTS {
            return Err(LibraryError::DebtTooHigh {
                member: member_id,
                cents: member.debt_cents,
            });
        }
        if self.loans_of(member_id) >= MAX_LOANS {
            return Err(LibraryError::TooManyLoans {
                member: member_id,
            });
        }

        let due_day = self.today + days;
        self.loans.push(Loan {
            item_code: code.to_string(),
            member_id,
            due_day,
        });
        Ok(due_day)
    }

    /// Returns an item and gives the late fee, in cents.
    pub fn give_back(
        &mut self,
        code: &str,
    ) -> Result<u32, LibraryError> {
        let pos = self
            .loans
            .iter()
            .position(|l| l.item_code == code)
            .ok_or_else(|| {
                LibraryError::NotBorrowed(code.into())
            })?;
        let loan = self.loans.remove(pos);

        let late_days =
            self.today.saturating_sub(loan.due_day);
        let fee =
            late_days * self.items[code].fee_per_day();
        if let Some(m) =
            self.members.get_mut(&loan.member_id)
        {
            m.debt_cents += fee;
        }
        Ok(fee)
    }

    pub fn pay(
        &mut self,
        member_id: u32,
        cents: u32,
    ) -> Result<u32, LibraryError> {
        let m = self.members.get_mut(&member_id).ok_or(
            LibraryError::UnknownMember(member_id),
        )?;
        m.debt_cents = m.debt_cents.saturating_sub(cents);
        Ok(m.debt_cents)
    }

    /// Loans whose due day has passed, oldest first.
    pub fn overdue(&self) -> Vec<&Loan> {
        let mut late: Vec<&Loan> = self
            .loans
            .iter()
            .filter(|l| l.due_day < self.today)
            .collect();
        late.sort_by_key(|l| l.due_day);
        late
    }

    /// Items whose title contains the text (any case).
    pub fn search(&self, text: &str) -> Vec<&dyn Item> {
        let text = text.to_lowercase();
        let mut found: Vec<&dyn Item> = self
            .items
            .values()
            .map(|b| b.as_ref())
            .filter(|i| {
                i.title().to_lowercase().contains(&text)
            })
            .collect();
        found.sort_by(|a, b| a.code().cmp(b.code()));
        found
    }

    /// Status of one item, for the report.
    fn status(&self, code: &str) -> String {
        let loan = self
            .loans
            .iter()
            .find(|l| l.item_code == code);
        match loan {
            Some(l) if l.due_day < self.today => {
                format!("LATE since {}", l.due_day)
            }
            Some(l) => {
                format!("out to day {}", l.due_day)
            }
            None if self.items[code]
                .can_be_borrowed() =>
            {
                "available".to_string()
            }
            None => "reference".to_string(),
        }
    }

    pub fn report(&self) -> String {
        let mut lines =
            vec![format!("--- Day {} ---", self.today)];
        let mut codes: Vec<&String> =
            self.items.keys().collect();
        codes.sort();
        for code in codes {
            let desc = self.items[code].describe();
            lines.push(format!(
                "{desc:<40}{}",
                self.status(code)
            ));
        }
        let mut ids: Vec<&u32> =
            self.members.keys().collect();
        ids.sort();
        for id in ids {
            let m = &self.members[id];
            lines.push(format!(
                "{:<6} loans: {}  owes: {}",
                m.name,
                self.loans_of(m.id),
                money(m.debt_cents)
            ));
        }
        lines.join("\n")
    }
}

#[cfg(test)]
#[path = "library_tests.rs"]
mod tests;
