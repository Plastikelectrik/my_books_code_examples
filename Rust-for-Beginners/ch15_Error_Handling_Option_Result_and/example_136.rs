// Book: Rust for Beginners — Example 136
fn main() {
    let good: Result<i32, String> = Ok(10);
    let bad: Result<i32, String> =
        Err("broken".to_string());

    println!("{}", good.clone().unwrap_or(0));
    println!("{}", bad.clone().unwrap_or(0));
    println!("{:?}", good.clone().map(|n| n * 2));
    println!(
        "{:?}",
        bad.clone().map_err(|e| e.to_uppercase())
    );
    println!("{:?}", bad.ok());

    let port: u16 =
        "8080x".parse().unwrap_or_else(|_| {
            println!("bad port, using default");
            3000
        });
    println!("port = {port}");
}
