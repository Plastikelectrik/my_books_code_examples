// Book: JavaScript for Absolute Beginners — Example 20
// queue-manager.js
const queue = [];
const done = [];

function addOrder(order) {
  queue.push(order);
  console.log(`+ ${order} (${queue.length} waiting)`);
}

function makeNext() {
  if (queue.length === 0) {
    console.log("Nothing to make. Time for a break!");
    return;
  }
  const order = queue.shift();
  done.push(order);
  console.log(`✔ Made ${order}`);
}

function showQueue() {
  if (queue.length === 0) {
    console.log("Queue is empty.");
    return;
  }
  console.log("Waiting:");
  for (const [i, order] of queue.entries()) {
    console.log(`  ${i + 1}. ${order}`);
  }
}

addOrder("latte for Sam");
addOrder("mocha for Priya");
addOrder("chai for Jo");
makeNext();
showQueue();
makeNext();
makeNext();
makeNext();
console.log(`Served today: ${done.join(", ")}`);
