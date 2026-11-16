mod storage;
mod task;

use std::env;
use std::path::Path;
use std::process;
use task::{Priority, TodoList};

const DATA_FILE: &str = "tasks.json";

enum Command {
    Add { title: String, priority: Priority },
    List,
    Done(u32),
    Remove(u32),
    Clean,
    Help,
}

fn parse_args(
    args: &[String],
) -> Result<Command, String> {
    let parse_id =
        |s: Option<&String>| -> Result<u32, String> {
            let s = s.ok_or("missing task number")?;
            s.parse().map_err(|_| {
                format!("'{s}' is not a number")
            })
        };
    match args.first().map(|s| s.as_str()) {
        None | Some("list") => Ok(Command::List),
        Some("add") => {
            let mut words = Vec::new();
            let mut priority = Priority::Normal;
            let mut it = args[1..].iter();
            while let Some(a) = it.next() {
                if a == "--priority" || a == "-p" {
                    let v = it
                        .next()
                        .ok_or("missing priority")?;
                    priority = Priority::parse(v).ok_or(
                        format!("unknown priority '{v}'"),
                    )?;
                } else {
                    words.push(a.as_str());
                }
            }
            if words.is_empty() {
                return Err(
                    "the task needs a title".into()
                );
            }
            Ok(Command::Add {
                title: words.join(" "),
                priority,
            })
        }
        Some("done") => {
            Ok(Command::Done(parse_id(args.get(1))?))
        }
        Some("remove") | Some("rm") => {
            Ok(Command::Remove(parse_id(args.get(1))?))
        }
        Some("clean") => Ok(Command::Clean),
        Some("help") | Some("--help") => {
            Ok(Command::Help)
        }
        Some(other) => {
            Err(format!("unknown command '{other}'"))
        }
    }
}

fn print_list(list: &TodoList) {
    if list.tasks().is_empty() {
        println!(
            "No tasks. Add one with: todo add <title>"
        );
        return;
    }
    for t in list.tasks() {
        let mark = if t.done { "x" } else { " " };
        let prio = format!("({})", t.priority);
        println!(
            "{:>3} [{mark}] {prio:<8} {}",
            t.id, t.title
        );
    }
    let total = list.tasks().len();
    println!(
        "{} of {total} tasks pending.",
        list.pending()
    );
}

fn print_help() {
    println!("Usage:");
    println!(
        "  todo add <title> [--priority low|normal|high]"
    );
    println!("  todo list");
    println!("  todo done <number>");
    println!("  todo remove <number>");
    println!("  todo clean    (remove completed tasks)");
}

fn run(
    command: Command,
    path: &Path,
) -> Result<(), String> {
    let mut list =
        storage::load(path).map_err(|e| e.to_string())?;
    let changed = match command {
        Command::Add { title, priority } => {
            let id = list.add(&title, priority);
            println!("Added task {id}: {title}");
            true
        }
        Command::List => {
            print_list(&list);
            false
        }
        Command::Done(id) => match list.complete(id) {
            Some(title) => {
                println!("Completed task {id}: {title}");
                true
            }
            None => {
                return Err(format!(
                    "no task number {id}"
                ));
            }
        },
        Command::Remove(id) => match list.remove(id) {
            Some(t) => {
                println!(
                    "Removed task {id}: {}",
                    t.title
                );
                true
            }
            None => {
                return Err(format!(
                    "no task number {id}"
                ));
            }
        },
        Command::Clean => {
            let n = list.clean();
            println!("Removed {n} completed task(s).");
            n > 0
        }
        Command::Help => {
            print_help();
            false
        }
    };
    if changed {
        storage::save(&list, path)
            .map_err(|e| e.to_string())?;
    }
    Ok(())
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    let result = parse_args(&args)
        .and_then(|cmd| run(cmd, Path::new(DATA_FILE)));
    if let Err(message) = result {
        eprintln!("Error: {message}");
        eprintln!("Try 'todo help'.");
        process::exit(1);
    }
}
