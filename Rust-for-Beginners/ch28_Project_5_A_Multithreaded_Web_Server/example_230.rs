// Book: Rust for Beginners — Example 230
use std::io::{BufRead, BufReader};
use std::net::TcpListener;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("cannot bind to port 7878");
    println!("Listening on http://127.0.0.1:7878");

    for stream in listener.incoming() {
        let stream = match stream {
            Ok(s) => s,
            Err(e) => {
                eprintln!("connection failed: {e}");
                continue;
            }
        };
        let reader = BufReader::new(&stream);
        let request: Vec<String> = reader
            .lines()
            .map_while(Result::ok)
            .take_while(|line| !line.is_empty())
            .collect();
        println!("Request: {request:#?}");
    }
}
