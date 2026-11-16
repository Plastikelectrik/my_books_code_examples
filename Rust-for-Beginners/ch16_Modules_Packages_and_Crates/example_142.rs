// Book: Rust for Beginners — Example 142
mod greetings {
    pub fn hello(name: &str) -> String {
        format!("Hello, {name}!")
    }

    pub fn goodbye(name: &str) -> String {
        format!("Goodbye, {name}. {}", farewell_wish())
    }

    // private: only usable inside this module
    fn farewell_wish() -> &'static str {
        "Have a nice day."
    }
}

fn main() {
    println!("{}", greetings::hello("Iris"));
    println!("{}", greetings::goodbye("Iris"));
}
