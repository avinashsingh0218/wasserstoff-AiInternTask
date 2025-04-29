let score = 0;
let history = [];

async function submitGuess() {
  const guess = document.getElementById("guessInput").value;
  const seed = "Rock"; // could make dynamic later

  const response = await fetch(`/game/guess?seed=${seed}&guess=${guess}&persona=cheery`, {
    method: "POST"
  });

  const data = await response.json();

  const resEl = document.getElementById("response");
  const scoreEl = document.getElementById("score");
  const histEl = document.getElementById("history");
  const globalEl = document.getElementById("global");

  if (data.error) {
    resEl.innerText = data.error;
  } else if (data.message.includes("Game Over")) {
    resEl.innerText = "Game Over!";
  } else {
    resEl.innerText = data.message;
    score += 1;
    history.push(guess);
    if (history.length > 5) history.shift();
    scoreEl.innerText = score;
    histEl.innerText = history.join(", ");
    globalEl.innerText = data.global_count || "-";
  }

  document.getElementById("guessInput").value = "";
}
