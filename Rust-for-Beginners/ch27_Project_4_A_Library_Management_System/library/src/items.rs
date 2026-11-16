/// Behavior shared by everything the library owns.
pub trait Item {
    fn code(&self) -> &str;
    fn title(&self) -> &str;
    fn kind(&self) -> &'static str;

    /// Days it can be borrowed. None = reference only.
    fn loan_days(&self) -> Option<u32>;

    /// Late fee per day, in cents.
    fn fee_per_day(&self) -> u32;

    /// One-line description (default implementation).
    fn describe(&self) -> String {
        format!(
            "[{}] {} ({})",
            self.code(),
            self.title(),
            self.kind()
        )
    }

    fn can_be_borrowed(&self) -> bool {
        self.loan_days().is_some()
    }
}

pub struct Book {
    pub code: String,
    pub title: String,
    pub author: String,
    pub pages: u32,
}

pub struct Film {
    pub code: String,
    pub title: String,
    pub minutes: u32,
}

pub struct Magazine {
    pub code: String,
    pub title: String,
    pub issue: u32,
}

impl Item for Book {
    fn code(&self) -> &str {
        &self.code
    }
    fn title(&self) -> &str {
        &self.title
    }
    fn kind(&self) -> &'static str {
        "book"
    }
    fn loan_days(&self) -> Option<u32> {
        Some(21)
    }
    fn fee_per_day(&self) -> u32 {
        20
    }
    fn describe(&self) -> String {
        format!(
            "[{}] {}, {} ({} p.)",
            self.code,
            self.title,
            self.author,
            self.pages
        )
    }
}

impl Item for Film {
    fn code(&self) -> &str {
        &self.code
    }
    fn title(&self) -> &str {
        &self.title
    }
    fn kind(&self) -> &'static str {
        "film"
    }
    fn loan_days(&self) -> Option<u32> {
        Some(7)
    }
    fn fee_per_day(&self) -> u32 {
        100
    }
    fn describe(&self) -> String {
        format!(
            "[{}] {}, {} min",
            self.code, self.title, self.minutes
        )
    }
}

impl Item for Magazine {
    fn code(&self) -> &str {
        &self.code
    }
    fn title(&self) -> &str {
        &self.title
    }
    fn kind(&self) -> &'static str {
        "magazine"
    }
    fn loan_days(&self) -> Option<u32> {
        None // reference only
    }
    fn fee_per_day(&self) -> u32 {
        0
    }
    fn describe(&self) -> String {
        format!(
            "[{}] {} #{}",
            self.code, self.title, self.issue
        )
    }
}
