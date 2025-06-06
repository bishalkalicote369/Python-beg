window.onload = () => {
  generateShuffledButtons();
};

function generateShuffledButtons() {
  const container = document.getElementById("number-buttons");
  container.innerHTML = "";

  const numbers = Array.from({ length: 9 }, (_, i) => i); // 0–99
  shuffle(numbers);

  numbers.forEach(num => {
    const btn = document.createElement("button");
    btn.textContent = num;
    btn.className = "number-btn";
    btn.onclick = () => {
      document.getElementById("password").value += num;
    };
    container.appendChild(btn);
  });
}

function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

function togglePassword() {
  const input = document.getElementById("password");
  input.type = input.type === "password" ? "text" : "password";
}

function clearPassword() {
  document.getElementById("password").value = "";
}

function submitForm() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  alert(`ईमेल: ${email}\nपासवर्ड: ${password}`);
  return false;
}
