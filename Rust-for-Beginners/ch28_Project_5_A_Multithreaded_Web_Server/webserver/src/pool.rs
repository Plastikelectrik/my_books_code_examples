use std::sync::mpsc::{self, Receiver, Sender};
use std::sync::{Arc, Mutex};
use std::thread::{self, JoinHandle};

/// A job: a closure that runs once on another thread.
type Job = Box<dyn FnOnce() + Send + 'static>;

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<Sender<Job>>,
}

struct Worker {
    id: usize,
    handle: Option<JoinHandle<()>>,
}

impl ThreadPool {
    /// Creates a pool with `size` worker threads.
    ///
    /// # Panics
    /// Panics if `size` is zero.
    pub fn new(size: usize) -> ThreadPool {
        assert!(
            size > 0,
            "a pool needs at least one thread"
        );
        let (sender, receiver) = mpsc::channel::<Job>();
        let receiver = Arc::new(Mutex::new(receiver));
        let workers = (0..size)
            .map(|id| {
                Worker::new(id, Arc::clone(&receiver))
            })
            .collect();
        ThreadPool { workers, sender: Some(sender) }
    }

    /// Sends a closure to be run by the next free worker.
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        if let Some(sender) = &self.sender {
            sender
                .send(Box::new(f))
                .expect("all workers stopped");
        }
    }
}

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<Receiver<Job>>>,
    ) -> Worker {
        let handle = thread::spawn(move || {
            loop {
                // The lock is released after this line
                let message =
                    receiver.lock().unwrap().recv();
                match message {
                    Ok(job) => {
                        println!(
                            "  worker {id} got a job"
                        );
                        job();
                    }
                    Err(_) => {
                        println!(
                            "  worker {id} shutting down"
                        );
                        break;
                    }
                }
            }
        });
        Worker { id, handle: Some(handle) }
    }
}

impl Drop for ThreadPool {
    /// Graceful shutdown: finish current jobs, then stop.
    fn drop(&mut self) {
        drop(self.sender.take()); // closes the channel
        for worker in &mut self.workers {
            if let Some(handle) = worker.handle.take() {
                handle.join().unwrap();
                println!(
                    "  worker {} stopped",
                    worker.id
                );
            }
        }
    }
}
