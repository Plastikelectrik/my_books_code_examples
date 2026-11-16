// Book: Rust for Beginners — Example 236
macro_rules! square_all {
    ( $( $x:expr ),* ) => {
        vec![ $( $x * $x ),* ]
    };
}

macro_rules! check {
    ($cond:expr) => {
        if $cond {
            println!("ok:     {}", stringify!($cond));
        } else {
            println!("FAILED: {}", stringify!($cond));
        }
    };
}

fn main() {
    let squares = square_all!(1, 2, 3, 4);
    println!("{squares:?}");

    check!(2 + 2 == 4);
    check!(squares.len() > 10);
}
