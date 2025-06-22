# train_spam_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Loading dataset
df = pd.read_csv("spam.csv", encoding='latin-1')[['label', 'message']]
df.columns = ['label', 'message']

# Encoding labels: spam = 1, ham = 0
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

# Splitting
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Vectorizing text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Training model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Testing
y_pred = model.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc:.2f}")

# Saving the model and vectorizer
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved!")
    
