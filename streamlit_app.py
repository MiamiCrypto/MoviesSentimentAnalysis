import streamlit as st
import pickle

# Load the sentiment analysis model
with open('SA_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_sentiment(text):
    """Predicts the sentiment of the given text."""
    prediction = model.predict([text])
    # Assuming the prediction returns an array with [0] for negative and [1] for positive sentiment
    sentiment = "Positive" if prediction[0] == 1 else "Negative"
    return sentiment

# Streamlit application UI
st.title('Sentiment Analysis Tool')

# Text input from the user
user_input = st.text_area("Enter text for sentiment analysis", "")

if st.button('Analyze'):
    if user_input:
        # Predict sentiment
        result = predict_sentiment(user_input)
        st.write(f"Sentiment: {result}")
    else:
        st.write("Please enter some text to analyze.")

# Instructions to run: Save this script as app.py and run it with the command `streamlit run app.py`.
