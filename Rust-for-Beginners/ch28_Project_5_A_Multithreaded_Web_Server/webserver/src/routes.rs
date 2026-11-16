use crate::http::{Method, Request, Response};
use std::thread;
use std::time::{Duration, SystemTime, UNIX_EPOCH};

fn page(title: &str, content: &str) -> String {
    format!(
        "<!DOCTYPE html><html><head>\
         <meta charset=\"utf-8\">\
         <title>{title}</title></head><body>\
         <h1>{title}</h1>{content}\
         <p><a href=\"/\">Home</a> | \
         <a href=\"/about\">About</a> | \
         <a href=\"/time\">Time</a></p></body></html>"
    )
}

/// Chooses the response for a request.
pub fn route(req: &Request) -> Response {
    if req.method != Method::Get {
        return Response::text(
            405,
            "Only GET is supported.",
        );
    }
    match req.path.as_str() {
        "/" => Response::html(
            200,
            page(
                "Hello from Rust!",
                "<p>This page was served by a \
                 web server written from scratch.</p>",
            ),
        ),
        "/about" => Response::html(
            200,
            page(
                "About",
                "<p>Built in Chapter 28 of \
                 <em>Rust for Beginners</em>.</p>",
            ),
        ),
        "/time" => {
            let secs = SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .map(|d| d.as_secs())
                .unwrap_or(0);
            let text =
                format!("<p>Unix time: {secs}</p>");
            Response::html(
                200,
                page("Server time", &text),
            )
        }
        "/slow" => {
            // Simulates a slow task (a big query...)
            thread::sleep(Duration::from_secs(3));
            Response::html(
                200,
                page("Slow page", "<p>Done!</p>"),
            )
        }
        path if path.starts_with("/hello/") => {
            let name = &path["/hello/".len()..];
            let safe = escape(name);
            Response::html(
                200,
                page(&format!("Hello, {safe}!"), ""),
            )
        }
        _ => {
            Response::html(404, page("404 Not Found", ""))
        }
    }
}

/// Escapes characters that have a meaning in HTML.
pub fn escape(text: &str) -> String {
    text.chars()
        .map(|c| match c {
            '<' => "&lt;".to_string(),
            '>' => "&gt;".to_string(),
            '&' => "&amp;".to_string(),
            '"' => "&quot;".to_string(),
            c => c.to_string(),
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashMap;

    fn get(path: &str) -> Request {
        Request {
            method: Method::Get,
            path: path.to_string(),
            headers: HashMap::new(),
        }
    }

    #[test]
    fn known_and_unknown_pages() {
        assert_eq!(route(&get("/")).status, 200);
        assert_eq!(route(&get("/about")).status, 200);
        assert_eq!(route(&get("/nope")).status, 404);
    }

    #[test]
    fn greeting_is_escaped() {
        let r = route(&get("/hello/<b>Bob</b>"));
        assert!(
            r.body.contains(
                "Hello, &lt;b&gt;Bob&lt;/b&gt;!"
            )
        );
    }
}
