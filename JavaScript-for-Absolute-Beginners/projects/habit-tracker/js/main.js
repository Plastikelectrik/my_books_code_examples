// js/main.js
import { dateKey, lastDays, shortDay } from "./dates.js";
import {
  createHabit, isDone, toggleDay, streak, validateName,
} from "./habits.js";
import { loadHabits, saveHabits } from "./storage.js";

let habits = loadHabits();

const list = document.querySelector("#habit-list");
const form = document.querySelector("#add-form");
const errorBox = document.querySelector("#form-error");

function renderDaysHeader(days) {
  const header = document.querySelector("#days-header");
  const cells = [document.createElement("span")];
  for (const day of days) {
    const span = document.createElement("span");
    span.textContent = shortDay(day);
    cells.push(span);
  }
  header.replaceChildren(...cells);
}

function habitRow(habit, days, todayKey) {
  const li = document.createElement("li");
  li.className = "habit row";
  li.dataset.id = habit.id;

  const name = document.createElement("span");
  name.textContent = `${habit.emoji} ${habit.name}`;
  li.append(name);

  for (const day of days) {
    const key = dateKey(day);
    const box = document.createElement("button");
    box.className = "day";
    box.dataset.day = key;
    box.textContent = day.getDate();
    if (isDone(habit, key)) box.classList.add("done");
    if (key === todayKey) box.classList.add("today");
    box.setAttribute("aria-pressed", isDone(habit, key));
    box.setAttribute("aria-label",
      `${habit.name}, ${day.toDateString()}`);
    li.append(box);
  }

  const badge = document.createElement("span");
  badge.className = "streak";
  const s = streak(habit);
  badge.textContent = s > 0 ? `🔥 ${s}` : "–";
  li.append(badge);

  const del = document.createElement("button");
  del.className = "delete";
  del.textContent = "✕";
  del.setAttribute("aria-label", `Delete ${habit.name}`);
  li.append(del);

  return li;
}

function render() {
  const days = lastDays(7);
  const todayKey = dateKey();

  renderDaysHeader(days);
  list.replaceChildren(
    ...habits.map((h) => habitRow(h, days, todayKey)),
  );

  const doneToday = habits
    .filter((h) => isDone(h, todayKey)).length;
  document.querySelector("#summary").textContent =
    habits.length === 0
      ? "Start by adding a habit."
      : `${doneToday} of ${habits.length} done today`;
  const empty = document.querySelector("#empty");
  empty.hidden = habits.length > 0;
}

function commit(newHabits) {
  habits = newHabits;
  saveHabits(habits);
  render();
}

list.addEventListener("click", (event) => {
  const row = event.target.closest(".habit");
  if (!row) return;
  const id = row.dataset.id;

  const dayButton = event.target.closest(".day");
  if (dayButton) {
    const key = dayButton.dataset.day;
    commit(habits.map((h) =>
      h.id === id ? toggleDay(h, key) : h));
    return;
  }

  if (event.target.closest(".delete")) {
    const habit = habits.find((h) => h.id === id);
    const question = `Delete "${habit.name}"?`;
    if (confirm(question)) {
      commit(habits.filter((h) => h.id !== id));
    }
  }
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = form.elements.name.value;
  const emoji = form.elements.emoji.value.trim() || "✅";

  const problem = validateName(name, habits);
  errorBox.textContent = problem ?? "";
  errorBox.hidden = problem === null;
  if (problem) return;

  commit([...habits, createHabit(name, emoji)]);
  form.reset();
  form.elements.name.focus();
});

render();
