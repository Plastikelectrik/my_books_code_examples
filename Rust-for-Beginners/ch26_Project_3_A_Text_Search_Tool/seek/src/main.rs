use seek::{Config, format_match, read_input, search};
use std::env;
use std::process;

const USAGE: &str =
    "usage: seek [-i] [-v] [-c] [-n] PATTERN [FILE...]";

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    let config = match Config::from_args(&args) {
        Ok(c) => c,
        Err(err) => {
            eprintln!("seek: {err}");
            eprintln!("{USAGE}");
            process::exit(2);
        }
    };

    let files = if config.files.is_empty() {
        vec!["-".to_string()] // no files: read stdin
    } else {
        config.files.clone()
    };
    let show_names = files.len() > 1;
    let opts = &config.options;

    let mut total = 0;
    let mut had_error = false;

    for path in &files {
        let text = match read_input(path) {
            Ok(t) => t,
            Err(e) => {
                eprintln!("seek: {e}");
                had_error = true;
                continue;
            }
        };
        let found = search(&config.query, &text, opts);
        total += found.len();

        if opts.count_only {
            if show_names {
                println!("{path}:{}", found.len());
            } else {
                println!("{}", found.len());
            }
            continue;
        }
        let name = if show_names {
            Some(path.as_str())
        } else {
            None
        };
        for m in &found {
            println!("{}", format_match(m, name, opts));
        }
    }

    // grep convention: 0 found, 1 not found, 2 error
    let code = if had_error {
        2
    } else if total > 0 {
        0
    } else {
        1
    };
    process::exit(code);
}
