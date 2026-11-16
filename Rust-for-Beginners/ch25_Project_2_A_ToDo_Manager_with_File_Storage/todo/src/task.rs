use serde::{Deserialize, Serialize};
use std::fmt;

#[derive(
    Debug,
    Clone,
    Copy,
    PartialEq,
    Eq,
    Serialize,
    Deserialize,
)]
pub enum Priority {
    Low,
    Normal,
    High,
}

impl Priority {
    pub fn parse(text: &str) -> Option<Priority> {
        match text.to_lowercase().as_str() {
            "low" | "l" => Some(Priority::Low),
            "normal" | "n" => Some(Priority::Normal),
            "high" | "h" => Some(Priority::High),
            _ => None,
        }
    }
}

impl fmt::Display for Priority {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let name = match self {
            Priority::Low => "low",
            Priority::Normal => "normal",
            Priority::High => "high",
        };
        write!(f, "{name}")
    }
}

#[derive(
    Debug, Clone, PartialEq, Serialize, Deserialize,
)]
pub struct Task {
    pub id: u32,
    pub title: String,
    pub done: bool,
    pub priority: Priority,
}

#[derive(Debug, Default, Serialize, Deserialize)]
pub struct TodoList {
    next_id: u32,
    tasks: Vec<Task>,
}

impl TodoList {
    pub fn new() -> Self {
        TodoList { next_id: 1, tasks: Vec::new() }
    }

    /// Adds a task and returns its new id.
    pub fn add(
        &mut self,
        title: &str,
        priority: Priority,
    ) -> u32 {
        let id = self.next_id.max(1);
        self.tasks.push(Task {
            id,
            title: title.trim().to_string(),
            done: false,
            priority,
        });
        self.next_id = id + 1;
        id
    }

    /// Marks a task as done. Returns its title if found.
    pub fn complete(&mut self, id: u32) -> Option<&str> {
        let task =
            self.tasks.iter_mut().find(|t| t.id == id)?;
        task.done = true;
        Some(&task.title)
    }

    /// Removes a task. Returns it if it existed.
    pub fn remove(&mut self, id: u32) -> Option<Task> {
        let pos =
            self.tasks.iter().position(|t| t.id == id)?;
        Some(self.tasks.remove(pos))
    }

    /// Removes all completed tasks. Returns how many.
    pub fn clean(&mut self) -> usize {
        let before = self.tasks.len();
        self.tasks.retain(|t| !t.done);
        before - self.tasks.len()
    }

    pub fn tasks(&self) -> &[Task] {
        &self.tasks
    }

    pub fn pending(&self) -> usize {
        self.tasks.iter().filter(|t| !t.done).count()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ids_increase_and_are_not_reused() {
        let mut list = TodoList::new();
        let a = list.add("a", Priority::Normal);
        let b = list.add("b", Priority::Normal);
        list.remove(b);
        let c = list.add("c", Priority::Normal);
        assert_eq!((a, b, c), (1, 2, 3));
    }

    #[test]
    fn complete_and_clean() {
        let mut list = TodoList::new();
        let id = list.add("write tests", Priority::High);
        list.add("relax", Priority::Low);
        assert_eq!(
            list.complete(id),
            Some("write tests")
        );
        assert_eq!(list.complete(99), None);
        assert_eq!(list.pending(), 1);
        assert_eq!(list.clean(), 1);
        assert_eq!(list.tasks().len(), 1);
    }

    #[test]
    fn priority_parsing() {
        assert_eq!(
            Priority::parse("HIGH"),
            Some(Priority::High)
        );
        assert_eq!(
            Priority::parse("n"),
            Some(Priority::Normal)
        );
        assert_eq!(Priority::parse("urgent"), None);
    }
}
