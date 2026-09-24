import streamlit as st
import re
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# ==============================
# Download NLTK Stopwords
# ==============================

NLTK_DATA_PATH = "/tmp/nltk_data"

nltk.data.path.append(NLTK_DATA_PATH)

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download(
        "stopwords",
        download_dir=NLTK_DATA_PATH,
        quiet=True
    )


# ==============================
# Load Model & Vectorizer
# ==============================

model = joblib.load("spam_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


# ==============================
# Text Preprocessing
# ==============================

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def stemming(text):
    words = text.split()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)


def preprocess_text(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stemming(text)
    return text


# ==============================
# Streamlit UI
# ==============================

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
