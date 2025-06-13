import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os

# STEP 1: Load CSV file (update path if needed)
df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

# STEP 2: Clean and preprocess
df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Convert to 0 or 1

# STEP 3: Split into features and labels
X = df['message']
y = df['label']

# STEP 4: Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 5: Convert text to numbers (TF-IDF better than CountVectorizer)
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# STEP 6: Train the model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# STEP 7: Test accuracy
y_pred = model.predict(X_test_vec)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

# STEP 8: Predict new message
def predict_message(msg):
    vec_msg = vectorizer.transform([msg])
    result = model.predict(vec_msg)
    return "Spam" if result[0] == 1 else "Not Spam"

# STEP 9: Let user test in terminal
while True:
    user_input = input("\nEnter an email/message to check (or type 'exit' to quit):\n> ")
    if user_input.lower() == 'exit':
        break
    print("Prediction:", predict_message(user_input))
