# 📧 Spam Detection System

## 🔍 Project Overview

The **Spam Detection System** is a supervised machine learning project that classifies emails or text messages as either **"spam"** or **"ham"** (not spam). It uses **Natural Language Processing (NLP)** techniques to transform text into numerical data and trains a **Logistic Regression** model for classification.

This project demonstrates how real-world problems like spam filtering can be solved using **text preprocessing**, **feature extraction (TF-IDF)**, and **classification algorithms** from `scikit-learn`.

---

## 🧱 Key Components

### ✅ Dependencies

The project uses:

- `pandas`, `numpy`: For data loading and manipulation  
- `scikit-learn`: For model building, preprocessing, and evaluation  
- `nltk`: For text cleaning and stopword removal (optional)

---

### 🗃️ Dataset and Preprocessing

- **Dataset**: A CSV file (`mail_data.csv`) containing labeled messages (`spam` or `ham`)
- **Null values** handled by replacing them with empty strings
- **Label Encoding**:
  - `spam` → `0`
  - `ham` → `1`
- **Text Preprocessing** includes:
  - Lowercasing
  - Removing punctuation
  - Vectorizing with TF-IDF

---

### 📐 Feature Extraction

- Used **TF-IDF Vectorization** to convert textual messages into numerical vectors  
- Transformed the input messages into a **sparse matrix** suitable for training

---

### 🧠 Model Training

- **Algorithm**: Logistic Regression
- **Training Process**:
  - Data split into training and test sets (typically 80/20)
  - Trained on TF-IDF features
- **Model Accuracy**:
  - ~96.70% on training data
  - ~96.59% on test data

---

### 🔁 Predictive System

- A prediction function allows users to input new messages and classify them as **spam** or **ham**
- Can be easily deployed via a **Flask API**, **CLI**, or simple **GUI**

---

## 🚀 Usage

### 📦 Prepare the Environment

```bash
pip install numpy pandas scikit-learn
```
---
### 🏃‍♂️ Run Training Script

- Load and preprocess data  
- Train the Logistic Regression model  
- Save the model using `joblib` (optional)

---

### 🔮 Predict New Messages

```python
model.predict(tfidf_vectorizer.transform(["Win a free iPhone now!"]))
```
---

## ✅ Conclusion

The **Spam Detection System** showcases the practical application of **Natural Language Processing (NLP)** and **Machine Learning (ML)** for a common real-world problem. It is:

- ✅ Lightweight  
- ✅ Accurate  
- ✅ Easily integrable into:

  - 📧 Email clients  
  - 📱 SMS applications  
  - 🖥️ Backend services for spam filtering

---

## 🙋‍♂️ Author

**Gaurav Pavtekar**  
🔗 [GitHub Profile](https://github.com/GURU-2471)  
📧 Email: gauravpavtekar24@gmail.com



