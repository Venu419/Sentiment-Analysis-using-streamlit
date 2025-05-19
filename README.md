
# 📊 Sentiment Analysis Web App

Welcome to the **Sentiment Analysis Web App**!  
This simple web application helps you figure out whether a sentence or a review is **Positive** or **Negative**. It's powered by **machine learning** and designed so that anyone—even with no coding experience—can use it easily.

---

## 🌟 What is Sentiment Analysis?

**Sentiment Analysis** is like teaching a computer to understand emotions in text. For example:
- "I love this product!" ➡️ Positive 😊  
- "This is the worst experience ever." ➡️ Negative 😞

This app does exactly that!

---

## 🛠️ What Does This App Do?

- You type in a sentence (like a review or opinion).
- The app cleans and processes the sentence using **Natural Language Processing (NLP)**.
- It then uses a **trained machine learning model** to predict if the text is **positive** or **negative**.
- You see the result instantly on your screen.

---

## 🧾 Files in the Project

- `app.py`: The main file that runs the Streamlit web app.
- `best_sentiment_model.pkl`: The trained ML model that understands the sentiment.
- `tfidf_vectorizer.pkl`: A tool that turns your sentence into a format the model can understand.

---

## 🚀 How to Run the Project

Here’s how you can run this project step by step:

### ✅ 1. Install Python
Make sure you have **Python** installed. You can download it from [python.org](https://www.python.org/).

### ✅ 2. Install Required Libraries

Open your terminal or command prompt and run:

```bash
pip install streamlit joblib nltk
```

### ✅ 3. Run the App

Make sure all three files (`app.py`, `best_sentiment_model.pkl`, and `tfidf_vectorizer.pkl`) are in the same folder.

In that folder, run this command:

```bash
streamlit run app.py
```

It will open the app in your browser automatically.

You can access the live from the [link](https://appuct-review-sentiment-analysis-frbbofaknnpoxj53czr6nq.streamlit.app/) here
---

## ✨ Example Use

Just type something like:

```
The product is really amazing and easy to use!
```

And click **Predict Sentiment**.  
You'll get an answer like:

**Sentiment: Positive** ✅

---

## 📚 How It Works (Simplified)

1. **Text Cleaning**: Removes common words like "the", "is", etc., and punctuation.
2. **Vectorizing**: Turns words into numbers so the model can understand them.
3. **Prediction**: The model guesses if the input is positive or negative.

---

## 👶 Who Can Use This?

Anyone! Whether you're a:
- Student
- Business owner checking reviews
- Curious beginner in machine learning

This app is for you.

---

## 🙌 Credits

- Built with [Streamlit](https://streamlit.io/)
- Uses [NLTK](https://www.nltk.org/) for text processing
- Machine learning with [scikit-learn](https://scikit-learn.org/)

---

Happy coding and have fun analyzing! 🎉

