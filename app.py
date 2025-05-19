import streamlit as st
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download NLTK data (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# Load the pre-trained model and vectorizer
model = joblib.load('best_sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

# Streamlit app
st.title("Sentiment Analysis Web App")

user_input = st.text_area("Enter your text here:")

if st.button("Predict Sentiment"):
    if user_input.strip():
        processed_text = preprocess_text(user_input)
        vect_text = vectorizer.transform([processed_text])
        prediction = model.predict(vect_text)
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        st.write(f"Sentiment: **{sentiment}**")
    else:
        st.write("Please enter some text to analyze.")
