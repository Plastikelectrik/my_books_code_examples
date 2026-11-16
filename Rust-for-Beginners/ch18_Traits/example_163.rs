// Book: Rust for Beginners — Example 163
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
#[derive(PartialOrd, Ord, Hash, Default)]
struct Version {
    major: u32,
    minor: u32,
    patch: u32,
}

fn main() {
    let v1 = Version { major: 1, minor: 4, patch: 2 };
    let v2 = Version { major: 1, minor: 10, patch: 0 };
    let v3 = v1; // Copy: v1 is still valid

    println!("{v1:?}");
    println!("v1 == v3: {}", v1 == v3); // PartialEq
    println!("v1 < v2: {}", v1 < v2); // PartialOrd
    println!("newest: {:?}", v1.max(v2)); // Ord
    println!("default: {:?}", Version::default());
}
