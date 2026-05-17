import pandas as pd
import re
import joblib
import streamlit as st
import nltk

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ── Load model once (cached so it only runs on first load) ────────────────────
@st.cache_resource
def load_model():
    model      = joblib.load('model.pkl')
    vector = joblib.load('vector.pkl')
    return model, vector

model, vector = load_model()

# ── Preprocessing (must match train_model.py exactly) ────────────────────────
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text: str) -> str:
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [ps.stem(w) for w in text if w not in stop_words]
    return ' '.join(text)

def predict(text: str) -> int:
    processed = preprocess(text)
    vec       = vector.transform([processed])
    return model.predict(vec)[0]

# ── UI ────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detector")
st.write("Paste a news headline or article excerpt below.")

input_text = st.text_area("News text", height=150, placeholder="Enter news here…")

if st.button("Check", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text first.")
    else:
        result = predict(input_text)
        if result == 1:
            st.success("✅ This looks like **Real News**")
        else:
            st.error("❌ This looks like **Fake News**")