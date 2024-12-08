function submitForm() {
  const urlInput = document.getElementById("features").value.trim();

  if (!urlInput) {
      alert("Please enter a URL.");
      return;
  }

  fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: urlInput }),
  })
      .then(response => response.json())
      .then(data => {
          const resultElement = document.getElementById("result");
          if (data.result) {
              resultElement.textContent = "Prediction: " + data.result;
          } else {
              resultElement.textContent = "Error: " + data.error;
          }
      })
      .catch(error => {
          console.error("Error:", error);
          document.getElementById("result").textContent = "Failed to get prediction.";
      });
}
