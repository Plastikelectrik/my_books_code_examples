// Book: Rust for Beginners — Example 64
struct Noisy {
    name: String,
}

impl Drop for Noisy {
    fn drop(&mut self) {
        println!("  (freeing {})", self.name);
    }
}

fn main() {
    println!("main starts");
    let _a = Noisy { name: String::from("A") };
    {
        println!("inner block starts");
        let _b = Noisy { name: String::from("B") };
        println!("inner block ends");
    } // _b goes out of scope here
    println!("main ends");
} // _a goes out of scope here
