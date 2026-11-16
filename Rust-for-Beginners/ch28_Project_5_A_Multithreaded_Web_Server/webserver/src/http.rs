use std::collections::HashMap;
use std::fmt;

#[derive(Debug, PartialEq, Clone, Copy)]
pub enum Method {
    Get,
    Post,
    Other,
}

#[derive(Debug, PartialEq)]
pub struct Request {
    pub method: Method,
    pub path: String,
    pub headers: HashMap<String, String>,
}

#[derive(Debug, PartialEq)]
pub enum ParseError {
    Empty,
    BadRequestLine(String),
}

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ParseError::Empty => {
                write!(f, "empty request")
            }
            ParseError::BadRequestLine(l) => {
                write!(f, "bad request line: '{l}'")
            }
        }
    }
}

impl Request {
    /// Parses the request line and headers.
    pub fn parse(
        lines: &[String],
    ) -> Result<Request, ParseError> {
        let first =
            lines.first().ok_or(ParseError::Empty)?;
        let parts: Vec<&str> =
            first.split_whitespace().collect();
        let [method, path, version] = parts.as_slice()
        else {
            return Err(ParseError::BadRequestLine(
                first.clone(),
            ));
        };
        if !version.starts_with("HTTP/") {
            return Err(ParseError::BadRequestLine(
                first.clone(),
            ));
        }
        let method = match *method {
            "GET" => Method::Get,
            "POST" => Method::Post,
            _ => Method::Other,
        };
        let mut headers = HashMap::new();
        for line in &lines[1..] {
            if let Some((name, value)) =
                line.split_once(':')
            {
                headers.insert(
                    name.trim().to_lowercase(),
                    value.trim().to_string(),
                );
            }
        }
        Ok(Request {
            method,
            path: path.to_string(),
            headers,
        })
    }
}

/// An HTTP response ready to be sent.
pub struct Response {
    pub status: u16,
    pub content_type: &'static str,
    pub body: String,
}

impl Response {
    pub fn html(status: u16, body: String) -> Self {
        Response {
            status,
            content_type: "text/html",
            body,
        }
    }

    pub fn text(status: u16, body: &str) -> Self {
        Response {
            status,
            content_type: "text/plain",
            body: body.to_string(),
        }
    }

    fn reason(&self) -> &'static str {
        match self.status {
            200 => "OK",
            400 => "Bad Request",
            404 => "Not Found",
            405 => "Method Not Allowed",
            _ => "Internal Server Error",
        }
    }

    /// The exact bytes to send over the connection.
    pub fn to_bytes(&self) -> Vec<u8> {
        format!(
            "HTTP/1.1 {} {}\r\n\
             Content-Type: {}; charset=utf-8\r\n\
             Content-Length: {}\r\n\
             Connection: close\r\n\r\n{}",
            self.status,
            self.reason(),
            self.content_type,
            self.body.len(),
            self.body
        )
        .into_bytes()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn lines(v: &[&str]) -> Vec<String> {
        v.iter().map(|s| s.to_string()).collect()
    }

    #[test]
    fn parses_a_get_request() {
        let req = Request::parse(&lines(&[
            "GET /about HTTP/1.1",
            "Host: localhost:7878",
            "User-Agent: test",
        ]))
        .unwrap();
        assert_eq!(req.method, Method::Get);
        assert_eq!(req.path, "/about");
        assert_eq!(req.headers["host"], "localhost:7878");
    }

    #[test]
    fn rejects_bad_requests() {
        assert_eq!(
            Request::parse(&[]),
            Err(ParseError::Empty)
        );
        let bad = lines(&["HELLO"]);
        assert!(Request::parse(&bad).is_err());
    }

    #[test]
    fn response_has_correct_length() {
        // é takes 2 bytes in UTF-8
        let r = Response::text(200, "héllo");
        let text =
            String::from_utf8(r.to_bytes()).unwrap();
        assert!(text.starts_with("HTTP/1.1 200 OK\r\n"));
        assert!(text.contains("Content-Length: 6\r\n"));
        assert!(text.ends_with("\r\n\r\nhéllo"));
    }
}
