// Book: Rust for Beginners — Example 208
use std::collections::HashMap;
use std::sync::mpsc;
use std::thread;

fn count_words(text: &str) -> HashMap<String, usize> {
    let mut counts = HashMap::new();
    for word in text.split_whitespace() {
        let w = word
            .trim_matches(|c: char| !c.is_alphanumeric())
            .to_lowercase();
        if !w.is_empty() {
            *counts.entry(w).or_insert(0) += 1;
        }
    }
    counts
}

fn main() {
    let documents = vec![
        "Rust is fast. Rust is safe.".to_string(),
        "Threads in Rust are safe threads.".to_string(),
        "Fast code, safe code, happy code!".to_string(),
        "Is it fast? It is.".to_string(),
    ];

    let (tx, rx) = mpsc::channel();
    let workers = 2;
    let chunk = documents.len().div_ceil(workers);

    for (id, part) in documents.chunks(chunk).enumerate()
    {
        let part = part.to_vec(); // owned copy
        let tx = tx.clone();
        thread::spawn(move || {
            let mut partial = HashMap::new();
            for doc in &part {
                for (w, n) in count_words(doc) {
                    *partial.entry(w).or_insert(0) += n;
                }
            }
            println!(
                "worker {id} processed {} docs",
                part.len()
            );
            tx.send(partial).unwrap();
        });
    }
    drop(tx);

    let mut total: HashMap<String, usize> =
        HashMap::new();
    for partial in rx {
        for (w, n) in partial {
            *total.entry(w).or_insert(0) += n;
        }
    }

    let mut top: Vec<_> = total.into_iter().collect();
    top.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    for (word, n) in top.iter().take(5) {
        println!("{word:<6} {n}");
    }
}
