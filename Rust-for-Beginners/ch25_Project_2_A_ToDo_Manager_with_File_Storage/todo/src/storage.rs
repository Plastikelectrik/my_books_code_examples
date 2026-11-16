use crate::task::TodoList;
use std::fmt;
use std::fs;
use std::io::ErrorKind;
use std::path::Path;

#[derive(Debug)]
pub enum StorageError {
    Io(std::io::Error),
    Format(serde_json::Error),
}

impl fmt::Display for StorageError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            StorageError::Io(e) => {
                write!(f, "file error: {e}")
            }
            StorageError::Format(e) => {
                write!(f, "invalid data file: {e}")
            }
        }
    }
}

// These From implementations let `?` convert errors
impl From<std::io::Error> for StorageError {
    fn from(e: std::io::Error) -> Self {
        StorageError::Io(e)
    }
}

impl From<serde_json::Error> for StorageError {
    fn from(e: serde_json::Error) -> Self {
        StorageError::Format(e)
    }
}

/// Loads the list. A missing file means an empty list.
pub fn load(
    path: &Path,
) -> Result<TodoList, StorageError> {
    match fs::read_to_string(path) {
        Ok(text) => Ok(serde_json::from_str(&text)?),
        Err(e) if e.kind() == ErrorKind::NotFound => {
            Ok(TodoList::new())
        }
        Err(e) => Err(e.into()),
    }
}

/// Saves the list as pretty-printed JSON.
pub fn save(
    list: &TodoList,
    path: &Path,
) -> Result<(), StorageError> {
    let json = serde_json::to_string_pretty(list)?;
    let tmp = path.with_extension("json.tmp");
    fs::write(&tmp, json)?;
    fs::rename(&tmp, path)?; // replace in one step
    Ok(())
}
