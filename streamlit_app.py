import streamlit as st
from textblob import TextBlob  # Assuming you're using TextBlob for sentiment analysis; replace with your model as necessary

st.title('Movie Review Sentiment Analysis')

# Text input from the user
user_input = st.text_area("Enter your movie review")

# Perform sentiment analysis in real-time
if user_input:
    sentiment = TextBlob(user_input).sentiment
    sentiment_score = sentiment.polarity  # Range from -1 to 1 where -1 is very negative and 1 is very positive

    # Determine sentiment color and emoji
    if sentiment_score > 0.1:  # Thresholds can be adjusted
        color = 'green'
        emoji = '🙂'
    elif sentiment_score < -0.1:
        color = 'red'
        emoji = '🙁'
    else:
        color = 'yellow'
        emoji = '😐'

    # Display the sentiment color and emoji
    st.markdown(f'<h1 style="color: {color};">{emoji} Sentiment Score: {sentiment_score:.2f}</h1>', unsafe_allow_html=True)
