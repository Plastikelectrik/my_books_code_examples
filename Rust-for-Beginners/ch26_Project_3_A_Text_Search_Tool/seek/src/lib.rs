//! seek: a small grep-like text search library.

use std::error::Error;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Read};

/// Search options chosen by the user.
#[derive(Debug, Default, Clone, PartialEq)]
pub struct Options {
    pub ignore_case: bool,
    pub invert: bool,
    pub count_only: bool,
    pub no_numbers: bool,
}

/// The complete configuration of one run.
#[derive(Debug, PartialEq)]
pub struct Config {
    pub query: String,
    pub files: Vec<String>,
    pub options: Options,
}

impl Config {
    /// Builds a Config from the arguments (without the
    /// program name). Flags may appear anywhere.
    pub fn from_args(
        args: &[String],
    ) -> Result<Config, String> {
        let mut options = Options::default();
        let mut positional = Vec::new();
        for arg in args {
            match arg.as_str() {
                "-i" => options.ignore_case = true,
                "-v" => options.invert = true,
                "-c" => options.count_only = true,
                "-n" => options.no_numbers = true,
                flag if flag.starts_with('-')
                    && flag.len() > 1 =>
                {
                    return Err(format!(
                        "unknown option '{flag}'"
                    ));
                }
                _ => positional.push(arg.clone()),
            }
        }
        if positional.is_empty() {
            return Err(
                "missing search pattern".to_string()
            );
        }
        let query = positional.remove(0);
        Ok(Config { query, files: positional, options })
    }
}

/// One matching line.
#[derive(Debug, PartialEq)]
pub struct Match<'a> {
    pub line_number: usize,
    pub line: &'a str,
}

/// Returns the lines of `text` that match `query`.
pub fn search<'a>(
    query: &str,
    text: &'a str,
    opts: &Options,
) -> Vec<Match<'a>> {
    let query_lower = query.to_lowercase();
    text.lines()
        .enumerate()
        .filter(|(_, line)| {
            let found = if opts.ignore_case {
                line.to_lowercase().contains(&query_lower)
            } else {
                line.contains(query)
            };
            found != opts.invert
        })
        .map(|(i, line)| Match {
            line_number: i + 1,
            line,
        })
        .collect()
}

/// Reads a whole input: a file path, or "-" for stdin.
pub fn read_input(
    path: &str,
) -> Result<String, Box<dyn Error>> {
    let mut text = String::new();
    if path == "-" {
        io::stdin().read_to_string(&mut text)?;
    } else {
        let file = File::open(path)
            .map_err(|e| format!("{path}: {e}"))?;
        let reader = BufReader::new(file);
        for line in reader.lines() {
            text.push_str(&line?);
            text.push('\n');
        }
    }
    Ok(text)
}

/// Formats one match for printing.
pub fn format_match(
    m: &Match,
    file: Option<&str>,
    opts: &Options,
) -> String {
    let mut out = String::new();
    if let Some(name) = file {
        out.push_str(name);
        out.push(':');
    }
    if !opts.no_numbers {
        out.push_str(&format!("{}: ", m.line_number));
    }
    out.push_str(m.line);
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEXT: &str = "Rust is fast.\n\
                        Python is easy.\n\
                        Rust is safe.\n\
                        trust the compiler";

    fn lines<'a>(found: &[Match<'a>]) -> Vec<&'a str> {
        found.iter().map(|m| m.line).collect()
    }

    #[test]
    fn finds_matching_lines() {
        let found =
            search("Rust", TEXT, &Options::default());
        assert_eq!(
            lines(&found),
            ["Rust is fast.", "Rust is safe."]
        );
        assert_eq!(found[1].line_number, 3);
    }

    #[test]
    fn ignoring_case() {
        let opts = Options {
            ignore_case: true,
            ..Options::default()
        };
        let found = search("rUsT", TEXT, &opts);
        assert_eq!(found.len(), 3); // includes "trust"
    }

    #[test]
    fn inverted_search() {
        let opts = Options {
            invert: true,
            ..Options::default()
        };
        let found = search("Rust", TEXT, &opts);
        assert_eq!(
            lines(&found),
            ["Python is easy.", "trust the compiler"]
        );
    }

    #[test]
    fn no_match_gives_empty_result() {
        let found =
            search("Java", TEXT, &Options::default());
        assert!(found.is_empty());
    }

    #[test]
    fn config_with_flags_anywhere() {
        let args: Vec<String> =
            ["-i", "word", "a.txt", "-c", "b.txt"]
                .iter()
                .map(|s| s.to_string())
                .collect();
        let cfg = Config::from_args(&args).unwrap();
        assert_eq!(cfg.query, "word");
        assert_eq!(cfg.files, ["a.txt", "b.txt"]);
        assert!(
            cfg.options.ignore_case
                && cfg.options.count_only
        );
    }

    #[test]
    fn config_errors() {
        assert!(Config::from_args(&[]).is_err());
        let bad =
            vec!["-x".to_string(), "word".to_string()];
        assert!(Config::from_args(&bad).is_err());
    }

    #[test]
    fn formatting() {
        let m = Match { line_number: 7, line: "hello" };
        let opts = Options::default();
        assert_eq!(
            format_match(&m, None, &opts),
            "7: hello"
        );
        assert_eq!(
            format_match(&m, Some("f.txt"), &opts),
            "f.txt:7: hello"
        );
    }
}
