// Book: Rust for Beginners — Example 154
#[derive(Debug)]
enum Loadable<T> {
    Loading,
    Ready(T),
    Failed(String),
}

fn describe<T: std::fmt::Debug>(
    item: &Loadable<T>,
) -> String {
    match item {
        Loadable::Loading => {
            String::from("please wait...")
        }
        Loadable::Ready(v) => format!("ready: {v:?}"),
        Loadable::Failed(why) => format!("failed: {why}"),
    }
}

fn main() {
    let profile: Loadable<&str> = Loadable::Ready("Ana");
    let scores: Loadable<Vec<u32>> = Loadable::Loading;
    let image: Loadable<u8> =
        Loadable::Failed("timeout".into());

    println!("{}", describe(&profile));
    println!("{}", describe(&scores));
    println!("{}", describe(&image));
}
