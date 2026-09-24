import streamlit as st
import pandas as pd
import re
import joblib

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# Download stopwords
# nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Stopwords
stop_words = set(stopwords.words('english'))

# Stemmer
stemmer = PorterStemmer()


def clean_text(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def remove_stopwords(text):
    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    return ' '.join(words)


def stemming(text):
    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
    ]

    return ' '.join(words)


def preprocess_text(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stemming(text)

    return text


# -------------------------
# Streamlit UI
# -------------------------

st.title("📱 Spam & Ham SMS Classifier")

st.write(
    "Enter an SMS message below to classify it as Spam or Ham."
)

message = st.text_area(
    "Enter your message:",
    height=150
)

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:

        processed_message = preprocess_text(message)

        vectorized_message = tfidf.transform(
            [processed_message]
        )

        prediction = model.predict(
            vectorized_message
        )[0]

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE")

        else:
            st.success("✅ HAM MESSAGE")