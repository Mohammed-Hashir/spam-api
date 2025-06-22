const API_URL = "https://spam-api-h431.onrender.com/predict";

// Add banner to email
function showBanner(prediction) {
    const existingBanner = document.getElementById("spam-banner");
    if (existingBanner) existingBanner.remove();
  
    const banner = document.createElement("div");
    banner.id = "spam-banner";
    banner.textContent = prediction === "Spam"
      ? "🚨 Warning: This email is classified as SPAM"
      : "✅ This email is classified as NOT SPAM";
  
    banner.style.padding = "12px";
    banner.style.fontWeight = "bold";
    banner.style.fontSize = "16px";
    banner.style.textAlign = "center";
    banner.style.color = "white";
    banner.style.backgroundColor = prediction === "Spam" ? "#d32f2f" : "#388e3c";
    banner.style.borderRadius = "8px";
    banner.style.margin = "12px";
    banner.style.zIndex = "9999";
  
    // Fallback: always try to place inside the visible email container
    const target = document.querySelector("div.a3s");
    if (target && target.parentElement) {
      target.parentElement.insertBefore(banner, target);
    } else {
      console.warn("⚠️ Could not find target for banner.");
    }
  }
  

function classifyOpenedEmail() {
  const emailBody = document.querySelector("div.a3s");
  if (!emailBody) return;

  const text = emailBody.innerText.trim();
  if (!text) return;

  fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: text }),
  })
    .then((res) => res.json())
    .then((data) => {
      showBanner(data.prediction);
    })
    .catch((err) => console.error("Prediction failed", err));
}

// Watch for email open
const observer = new MutationObserver(() => {
  const emailView = document.querySelector("div.a3s");
  if (emailView) {
    classifyOpenedEmail();
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true,
});
