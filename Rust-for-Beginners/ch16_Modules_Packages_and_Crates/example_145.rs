// Book: Rust for Beginners — Example 145
mod kitchen {
    pub fn cook() -> String {
        format!(
            "{} and {}",
            self::prepare(),
            super::serve()
        )
    }

    fn prepare() -> &'static str {
        "chopping"
    }
}

fn serve() -> &'static str {
    "serving"
}

fn main() {
    println!("{}", crate::kitchen::cook());
}
