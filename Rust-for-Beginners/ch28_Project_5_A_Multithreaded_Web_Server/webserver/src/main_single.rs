mod http;
mod routes;

use http::{Request, Response};
use std::io::{BufRead, BufReader, Write};
use std::net::{TcpListener, TcpStream};

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
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("cannot bind to port 7878");
    println!("Listening on http://127.0.0.1:7878");
    for stream in listener.incoming().flatten() {
        handle(stream);
    }
}
