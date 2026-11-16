// Book: Rust for Beginners — Example 149
use rand::seq::IndexedRandom;

fn main() {
    // A random number between 1 and 6, like a die
    let roll: u32 = rand::random_range(1..=6);
    println!("You rolled a {roll}");

    // A random true or false
    let heads: bool = rand::random();
    println!("Heads? {heads}");

    // A random element from a list
    let meals = ["pasta", "curry", "salad", "tacos"];
    let mut rng = rand::rng();
    let dinner = meals.choose(&mut rng).unwrap();
    println!("Tonight we eat {dinner}");
}
