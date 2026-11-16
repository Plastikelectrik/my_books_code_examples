// Book: Rust for Beginners — Example 246
fn double_all(numbers: &mut Vec<i32>) {
    for n in numbers.iter_mut() {
        *n *= 2;
    }
}

fn swap(a: &mut i32, b: &mut i32) {
    let tmp = *a;
    *a = *b;
    *b = tmp;
}

fn main() {
    let mut v = vec![1, 2, 3];
    double_all(&mut v);
    println!("{v:?}");

    let (mut x, mut y) = (1, 2);
    swap(&mut x, &mut y);
    println!("x = {x}, y = {y}");
}
