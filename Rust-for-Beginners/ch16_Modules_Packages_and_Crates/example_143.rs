// Book: Rust for Beginners — Example 143
mod shop {
    pub struct Price {
        cents: u32, // private field
    }

    impl Price {
        pub fn new(cents: u32) -> Self {
            Price { cents }
        }

        pub fn with_discount(
            &self,
            percent: u32,
        ) -> Price {
            let p = percent.min(100);
            Price { cents: self.cents * (100 - p) / 100 }
        }

        pub fn display(&self) -> String {
            format!(
                "{}.{:02}",
                self.cents / 100,
                self.cents % 100
            )
        }
    }
}

fn main() {
    let p = shop::Price::new(2_500);
    let sale = p.with_discount(30);
    println!("{} -> {}", p.display(), sale.display());
    // shop::Price { cents: 10 }; // error: private
}
