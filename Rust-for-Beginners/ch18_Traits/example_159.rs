// Book: Rust for Beginners — Example 159
trait Describe {
    fn name(&self) -> String;

    // default: uses name()
    fn describe(&self) -> String {
        format!("This is {}.", self.name())
    }
}

struct Cat;
struct Planet {
    name: String,
    moons: u32,
}

impl Describe for Cat {
    fn name(&self) -> String {
        String::from("a cat")
    }
    // uses the default describe()
}

impl Describe for Planet {
    fn name(&self) -> String {
        self.name.clone()
    }

    // overrides the default
    fn describe(&self) -> String {
        format!("{} has {} moons.", self.name, self.moons)
    }
}

fn main() {
    let earth = Planet { name: "Earth".into(), moons: 1 };
    println!("{}", Cat.describe());
    println!("{}", earth.describe());
}
