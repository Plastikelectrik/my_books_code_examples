mod http;
mod pool;
mod routes;

use http::{Request, Response};
use pool::ThreadPool;
use std::env;
use std::io::{BufRead, BufReader, Write};
use std::net::{TcpListener, TcpStream};

const ADDRESS: &str = "127.0.0.1:7878";
const WORKERS: usize = 4;

fn handle(mut stream: TcpStream) {
    let reader = BufReader::new(&stream);
    let lines: Vec<String> = reader
        .lines()
        .map_while(Result::ok)
        .take_while(|l| !l.is_empty())
        .collect();

    let response = match Request::parse(&lines) {
        Ok(req) => {
            println!("{:?} {}", req.method, req.path);
            routes::route(&req)
        }
        Err(e) => Response::text(400, &e.to_string()),
    };
    if let Err(e) = stream.write_all(&response.to_bytes())
    {
        eprintln!("write failed: {e}");
    }
}

fn main() {
    let limit: Option<usize> =
        env::args().nth(1).and_then(|a| a.parse().ok());

    let listener = TcpListener::bind(ADDRESS)
        .unwrap_or_else(|e| {
            eprintln!("cannot listen on {ADDRESS}: {e}");
            std::process::exit(1);
        });
    let pool = ThreadPool::new(WORKERS);
    println!(
        "Serving http://{ADDRESS} with {WORKERS} workers"
    );

    let connections = listener.incoming().flatten();
    let connections: Box<dyn Iterator<Item = TcpStream>> =
        match limit {
            Some(n) => Box::new(connections.take(n)),
            None => Box::new(connections),
        };
    for stream in connections {
        pool.execute(move || handle(stream));
    }

    println!("Request limit reached, shutting down.");
} // pool is dropped here: graceful shutdown
