# 📱 Spam & Ham SMS Classifier using NLP and Machine Learning

An end-to-end Natural Language Processing (NLP) and Machine Learning project that classifies SMS messages as **Spam** or **Ham** using text preprocessing, TF-IDF vectorization, and Linear SVM.

## 🌐 Live Demo

🚀 **Try the deployed application:**

[Open Spam & Ham SMS Classifier](https://spam-ham-sms-classifier-using-nlp-and-machine-learning-dcljt6t.streamlit.app/)

---

## 📌 Project Overview

This project analyzes SMS messages and builds a machine learning model to automatically classify messages as:

- ✅ **Ham** – Normal/legitimate SMS
- 🚨 **Spam** – Unwanted or promotional SMS

The project covers the complete workflow from data exploration and preprocessing to machine learning, evaluation, and deployment.

---

## 🎯 Objectives

- Analyze and understand the SMS dataset
- Clean and preprocess text data
- Explore characteristics of Spam and Ham messages
- Convert text into numerical features using TF-IDF
- Train multiple machine learning classification models
- Compare model performance using evaluation metrics
- Select the final model
- Deploy the model using Streamlit

---

## 🔄 Project Workflow

```text
SMS Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Text Preprocessing
     ↓
Stopword Removal
     ↓
Stemming
     ↓
TF-IDF Vectorization
     ↓
Machine Learning Models
     ↓
Model Evaluation
     ↓
Linear SVM Selection
     ↓
Streamlit Deployment
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- TF-IDF
- Linear SVM
- Streamlit
- Joblib

---

## 📊 Dataset

The dataset contains two main columns:

- `Category`
- `Message`


---

## 🧹 Text Preprocessing

The following preprocessing steps were applied:

1. Convert text to lowercase
2. Remove URLs
3. Remove special characters and numbers
4. Remove extra spaces
5. Remove English stopwords
6. Apply Porter stemming

### Preprocessing Pipeline

```text
Raw SMS
   ↓
Lowercase
   ↓
Remove URLs
   ↓
Remove Special Characters
   ↓
Remove Stopwords
   ↓
Stemming
   ↓
Clean Text
```

---

## 🤖 Machine Learning Models

Three classification models were trained and evaluated:

1. Naive Bayes
2. Logistic Regression
3. Linear SVM

### Model Comparison

| Rank | Model | Accuracy | Precision | Recall | F1 Score |
|------|-------|----------|-----------|--------|----------|
| 1 | Linear SVM | 97.48% | 94.74% | 84.38% | 89.26% |
| 2 | Naive Bayes | 96.22% | 100.00% | 69.53% | 82.03% |
| 3 | Logistic Regression | 96.12% | 96.81% | 71.09% | 81.98% |

**Linear SVM was selected as the final model based on the highest F1-score among the evaluated models.**

---

## 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

## 🧠 Final NLP Architecture

```text
                SMS Message
                     │
                     ▼
              Text Cleaning
                     │
                     ▼
             Stopword Removal
                     │
                     ▼
                 Stemming
                     │
                     ▼
              TF-IDF Vectorizer
                     │
                     ▼
                Linear SVM
                     │
             ┌───────┴───────┐
             ▼               ▼
          🚨 Spam          ✅ Ham
```

---

## 🌐 Streamlit Application

The trained model was integrated into a Streamlit web application.

Users can enter an SMS message and click **Predict** to classify the message.

### Application Flow

```text
User enters SMS
       ↓
Text Preprocessing
       ↓
TF-IDF Transformation
       ↓
Linear SVM Prediction
       ↓
Spam / Ham Result
```

---

## 🖥️ Application Output

### 🚨 Spam Prediction


### ✅ Ham Prediction

---

## 📂 Project Structure

```text
spam-ham-sms-classifier-using-nlp-and-machine-learning/
│
├── app.py
├── Spam and Ham.ipynb
├── spam_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── spam_output.png
    └── ham_output.png
```

---

## ▶️ Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/spam-ham-sms-classifier-using-nlp-and-machine-learning.git
```

### 2. Navigate to the Project Directory

```bash
cd spam-ham-sms-classifier-using-nlp-and-machine-learning
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 📦 Required Libraries

```text
streamlit
pandas
numpy
scikit-learn
nltk
joblib
```

---

## 🚀 Future Improvements

- Experiment with Word2Vec and other word embeddings
- Test deep learning-based NLP models
- Add more diverse SMS datasets
- Improve handling of URLs and phone numbers
- Add more evaluation visualizations
- Improve the Streamlit user interface

---

## 👩‍💻 Author

**Gorli Sanjana**

B.Tech – Computer Science & Engineering

Interested in **Data Science, Machine Learning, NLP, and Generative AI**.

---

## 🔗 Project Links

🚀 **Live Application:**

[Spam & Ham SMS Classifier](https://spam-ham-sms-classifier-using-nlp-and-machine-learning-dcljt6t.streamlit.app/)
