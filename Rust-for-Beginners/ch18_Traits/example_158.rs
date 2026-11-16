// Book: Rust for Beginners — Example 158
trait Summary {
    fn summarize(&self) -> String;
}

struct Article {
    title: String,
    author: String,
    words: u32,
}

struct Tweet {
    user: String,
    text: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!(
            "{} by {} ({} words)",
            self.title, self.author, self.words
        )
    }
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("@{}: {}", self.user, self.text)
    }
}

fn main() {
    let a = Article {
        title: "Rust in Space".into(),
        author: "N. Okafor".into(),
        words: 1800,
    };
    let t = Tweet {
        user: "ferris".into(),
        text: "Just compiled on the first try!".into(),
    };
    println!("{}", a.summarize());
    println!("{}", t.summarize());
}
