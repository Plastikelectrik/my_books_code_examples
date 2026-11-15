// quiz.js
const QUESTIONS = [
  {
    text: "Which country produces the most coffee?",
    options: [
      "Colombia", "Ethiopia", "Brazil", "Vietnam",
    ],
    answer: 2,
    explain: "Brazil has led production for decades.",
  },
  {
    text: "What is a 'flat white' made with?",
    options: [
      "Espresso and microfoam milk",
      "Filter coffee and cream",
      "Espresso and hot water",
      "Cold brew and milk",
    ],
    answer: 0,
    explain: "Espresso with thin, velvety microfoam.",
  },
  {
    text: "Where did coffee plants originally grow wild?",
    options: ["Ethiopia", "Italy", "India", "Mexico"],
    answer: 0,
    explain: "Wild coffee plants originated in Ethiopia.",
  },
  {
    text: "What does 'barista' mean in Italian?",
    options: [
      "Coffee maker", "Bartender", "Waiter", "Chef",
    ],
    answer: 1,
    explain: "In Italy, a barista works behind a bar.",
  },
  {
    text: "Which drink is espresso with steamed milk "
      + "and a thick layer of foam?",
    options: [
      "Americano", "Cortado", "Cappuccino", "Lungo",
    ],
    answer: 2,
    explain: "A cappuccino has the thickest foam layer.",
  },
];

const state = {
  index: 0,        // which question we are on
  score: 0,
  answered: false, // current question answered?
};

const screens = {
  start: document.querySelector("#start-screen"),
  question: document.querySelector("#question-screen"),
  result: document.querySelector("#result-screen"),
};

function showScreen(name) {
  for (const [key, element] of Object.entries(screens)) {
    element.classList.toggle("hidden", key !== name);
  }
}

function renderQuestion() {
  const q = QUESTIONS[state.index];
  state.answered = false;

  document.querySelector("#progress").textContent =
    `Question ${state.index + 1} of ${QUESTIONS.length}` +
    ` · Score: ${state.score}`;
  document.querySelector("#question-text").textContent =
    q.text;

  const buttons = q.options.map((option, i) => {
    const button = document.createElement("button");
    button.textContent = option;
    button.dataset.index = i;
    return button;
  });
  document.querySelector("#options")
    .replaceChildren(...buttons);

  document.querySelector("#explanation")
    .classList.add("hidden");
  document.querySelector("#next-btn")
    .classList.add("hidden");
}

const optionsBox = document.querySelector("#options");

optionsBox.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button || state.answered) return;
  checkAnswer(Number(button.dataset.index));
});

function checkAnswer(chosen) {
  const q = QUESTIONS[state.index];
  state.answered = true;
  const isRight = chosen === q.answer;
  if (isRight) state.score++;

  const buttons = optionsBox.querySelectorAll("button");
  buttons.forEach((button, i) => {
    button.disabled = true;
    if (i === q.answer) button.classList.add("correct");
    if (i === chosen && !isRight) {
      button.classList.add("wrong");
    }
  });

  const verdict = isRight ? "✅ Correct!" : "❌ Not quite.";
  const box = document.querySelector("#explanation");
  box.textContent = `${verdict} ${q.explain}`;
  box.classList.remove("hidden");

  const next = document.querySelector("#next-btn");
  next.textContent = state.index === QUESTIONS.length - 1
    ? "See my score"
    : "Next question";
  next.classList.remove("hidden");
  next.focus();
}

document.querySelector("#next-btn")
  .addEventListener("click", () => {
    state.index++;
    if (state.index < QUESTIONS.length) {
      renderQuestion();
    } else {
      showResult();
    }
  });

const BEST_KEY = "copperKettle.quiz.best";

function loadBest() {
  return Number(localStorage.getItem(BEST_KEY)) || 0;
}

function showResult() {
  const total = QUESTIONS.length;
  const best = loadBest();
  const isNewBest = state.score > best;
  if (isNewBest) {
    localStorage.setItem(BEST_KEY, String(state.score));
  }

  const ratio = state.score / total;
  let title;
  if (ratio === 1) title = "Perfect! A true expert ☕";
  else if (ratio >= 0.6) title = "Great job!";
  else title = "Keep sipping and learning!";

  const heading = document.querySelector("#result-title");
  heading.textContent = title;
  document.querySelector("#result-text").textContent =
    `You scored ${state.score} out of ${total}.` +
    (isNewBest
      ? " New best! Show this screen for a free biscuit."
      : ` The best score is ${best}.`);
  showScreen("result");
}

function startQuiz() {
  state.index = 0;
  state.score = 0;
  showScreen("question");
  renderQuestion();
}

function renderStart() {
  const best = loadBest();
  document.querySelector("#best-score").textContent =
    best > 0
      ? `Best score so far: ${best} / ${QUESTIONS.length}`
      : "Be the first to set a best score!";
  showScreen("start");
}

document.querySelector("#start-btn")
  .addEventListener("click", startQuiz);
document.querySelector("#again-btn")
  .addEventListener("click", startQuiz);

renderStart();
