# app.py

from flask import Flask, request, jsonify
import pickle

# Load model and vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Spam Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    # Vectorize input message
    vect_msg = vectorizer.transform([message])
    
    # Predict
    prediction = model.predict(vect_msg)[0]
    label = "Spam" if prediction == 1 else "Not Spam"

    return jsonify({"prediction": label})

if __name__ == "__main__":
    app.run(debug=True)
