import streamlit as st
from textblob import TextBlob  # Replace with your model as necessary

# Streamlit page configuration
st.set_page_config(page_title="Movie Review Sentiment Analysis", page_icon="🎬")

st.title('Movie Review Sentiment Analysis')

# Display an image from a file with adjustable size
st.subheader("Movie Revenue Prediction")
image_size = st.slider("Select the image size", 100, 500, 300)  # min_value, max_value, default_value
st.image("https://raw.githubusercontent.com/your_username/your_repository/main/path_to/Aiface3.png",
         width=image_size,
         caption="Predict your favorite movie's revenue")

# Text input from the user for sentiment analysis
user_input = st.text_area("Enter your movie review")

# Button to trigger sentiment analysis
if st.button('Analyze Sentiment'):
    if user_input:
        sentiment = TextBlob(user_input).sentiment
        sentiment_score = sentiment.polarity  # Range from -1 to 1

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

        # Display the sentiment color, emoji, and score
        st.markdown(f'<h1 style="color: {color};">{emoji} Sentiment Score: {sentiment_score:.2f}</h1>',
                    unsafe_allow_html=True)
