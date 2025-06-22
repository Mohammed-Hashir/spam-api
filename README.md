# 📧 Gmail Spam Detector Extension
Detect spam emails in Gmail in real-time using a trained machine learning model.

# 🚀 Features
✅ Automatically scans opened emails on Gmail

📊 Uses a trained Naive Bayes classifier (trained on spam.csv)

📦 Real-time predictions using a Flask API

# 🔍 Displays a banner on each email:
Red warning if spam

Green safe flag if not spam

# 🧠 ML Model
Model: Multinomial Naive Bayes

Vectorization: TfidfVectorizer

Dataset used: spam.csv

Accuracy: ~98%

Model and vectorizer saved as:

spam_model.pkl

vectorizer.pkl

# 🧪 Backend API
Built with Flask, hosted via Render:

POST /predict

Body: { "message": "Your message here" }

Response: { "prediction": "Spam" | "Not Spam" }

# 📦 Files Included
File	Description

train_spam_model.py	Trains and saves the ML model

app.py	Flask API to serve predictions

spam_model.pkl	Trained model

vectorizer.pkl	TF-IDF vectorizer

requirements.txt	All required Python dependencies

manifest.json	Chrome extension manifest

content.js	Gmail content script to classify email

popup.html (optional)	Extension popup interface

# 🧩 Extension Setup
Go to brave://extensions or chrome://extensions

Enable Developer Mode

Click "Load Unpacked"

Select the folder with manifest.json

# ⚙️ How It Works
When you open an email, the extension grabs the email content.

It sends the message to your hosted Flask API (/predict endpoint).

API returns "Spam" or "Not Spam".

A banner is injected above the email body to inform the user.

# 🖼️ Example
Banner shows red alert for spam email.

Banner shows green check for non-spam email.

# 🔐 Permissions Used
"activeTab" – to read Gmail content

"scripting" – to inject DOM elements (banner)

"https://mail.google.com/*" – Gmail specific access

### 👨‍💻 Built With
* Python

* Scikit-learn

* Pandas 

* Streamlit

* Flask

* Flask_CORS

* Js

* Json

* HTML (optional)

# 📬 Contact
Feel free to connect with me on [LinkedIn](www.linkedin.com/in/mohammed-hashir-99793428a) or \[[email@example.com](mailto:smdhashir2006@gmail.com)]
