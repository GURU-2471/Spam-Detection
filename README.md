📧 Spam Detection System

🔍 Project Overview
The Spam Detection System is a supervised machine learning project that classifies emails or text messages as either "spam" or "ham" (not spam). It uses natural language processing (NLP) techniques to transform text into numerical data and trains a Logistic Regression model for classification.

This project demonstrates how real-world problems like spam filtering can be solved using text preprocessing, feature extraction (TF-IDF), and classification algorithms from scikit-learn.

🧱 Key Components

✅ Dependencies
The project uses:

pandas, numpy: For data loading and manipulation

scikit-learn: For model building, preprocessing, and evaluation

nltk: For text cleaning and stopword removal (optional)

🗃️ Dataset and Preprocessing
Dataset: A CSV file (mail_data.csv) containing labeled messages (spam or ham)

Null values handled by replacing with empty strings

Label encoding:

spam → 0

ham → 1

Text preprocessing includes lowercasing, removing punctuation, and vectorizing

📐 Feature Extraction
Used TF-IDF Vectorization to convert textual messages into numerical vectors

Transformed the input messages into a sparse matrix for training

🧠 Model Training
Algorithm: Logistic Regression

Training:

Data split into training and test sets (typically 80/20)

Trained on TF-IDF features

Model achieved:

~96.70% accuracy on training data

~96.59% accuracy on test data

🔁 Predictive System
A prediction function allows users to input new messages and classify them as spam or ham using the trained model

Can be easily deployed via a Flask API or GUI for end users

🚀 Usage
1. Prepare the Environment
bash
Copy
Edit
pip install numpy pandas scikit-learn
2. Run Training Script
Load and preprocess data

Train Logistic Regression model

Save model using joblib (optional)

3. Predict New Messages
python
Copy
Edit
model.predict(tfidf_vectorizer.transform(["Win a free iPhone now!"]))

✅ Conclusion
The Spam Detection System showcases the practical application of NLP and ML for a common problem. It is lightweight, accurate, and can be integrated into email clients, SMS apps, or backend services for spam filtering.

