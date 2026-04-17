async function sendQuestion() {
  const question = document.getElementById("question").value;
  const response = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      question,
      session_id: "browser-demo"
    })
  });
  const data = await response.json();

  document.getElementById("result").hidden = false;
  document.getElementById("answer").innerText = data.answer;

  const list = document.getElementById("citations");
  list.innerHTML = "";
  for (const citation of data.citations) {
    const item = document.createElement("li");
    item.innerText = `${citation.source}: ${citation.snippet}`;
    list.appendChild(item);
  }
}

document.getElementById("send").addEventListener("click", sendQuestion);
