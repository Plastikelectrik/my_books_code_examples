// Book: Rust for Beginners — Example 26
fn main() {
    let total_cake = 17;
    let people = 5;

    let whole_pieces = total_cake / people;
    let leftover = total_cake % people;
    let exact = total_cake as f64 / people as f64;

    println!("Each person gets {whole_pieces} pieces");
    println!("Pieces left over: {leftover}");
    println!("Exact share: {exact}");
}
