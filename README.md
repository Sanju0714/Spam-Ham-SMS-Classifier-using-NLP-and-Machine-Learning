# 📱 Spam & Ham SMS Classifier

An end-to-end NLP and Machine Learning project that classifies SMS messages as **Spam** or **Ham** using text preprocessing, TF-IDF vectorization, and Linear SVM.

## 🌐 Live Demo

🚀 [Try the Live Application](https://spam-ham-sms-classifier-using-nlp-and-machine-learning-dcljt6t.streamlit.app/)

## 📌 Project Overview

This project uses Natural Language Processing and Machine Learning to classify SMS messages into:

- ✅ **Ham** – Normal/legitimate messages
- 🚨 **Spam** – Unwanted or promotional messages

## 🔄 Project Workflow

```text
SMS Dataset
     ↓
Data Cleaning & EDA
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
Linear SVM
     ↓
Streamlit Deployment
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
NLTK
Scikit-learn
TF-IDF
Linear SVM
Streamlit
Joblib
🤖 Machine Learning Models
Naive Bayes
Logistic Regression
Linear SVM
📊 Model Performance
Model	Accuracy	Precision	Recall	F1 Score
Linear SVM	97.48%	94.74%	84.38%	89.26%
Naive Bayes	96.22%	100.00%	69.53%	82.03%
Logistic Regression	96.12%	96.81%	71.09%	81.98%

Linear SVM was selected as the final model based on the highest F1-score.

🧠 NLP Pipeline
Raw SMS
   ↓
Text Cleaning
   ↓
Stopword Removal
   ↓
Stemming
   ↓
TF-IDF
   ↓
Linear SVM
   ↓
Spam / Ham
🖥️ Streamlit Application

The trained model is deployed using Streamlit. Users can enter an SMS message and receive a Spam or Ham prediction.

Application Output

📂 Project Structure
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
▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py
🎯 Key Skills
Exploratory Data Analysis
Natural Language Processing
Text Preprocessing
TF-IDF Vectorization
Machine Learning
Model Evaluation
Streamlit Deployment
🚀 Future Improvements
Experiment with word embeddings
Explore deep learning-based NLP models
Add more SMS data
Improve the Streamlit interface
👩‍💻 Author

Gorli Sanjana

B.Tech – Computer Science & Engineering

Data Science | Machine Learning | NLP | Generative AI
