// Book: Rust for Beginners — Example 180
fn main() {
    let v = vec![1, 2, 3];

    // Nothing happens yet: no consumer
    let pipeline = v.iter().map(|x| {
        println!("  processing {x}");
        x * 10
    });

    println!("pipeline created, nothing processed yet");
    let result: Vec<i32> = pipeline.collect();
    println!("result: {result:?}");
}
