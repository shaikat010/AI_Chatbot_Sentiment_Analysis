import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only needs to be done once)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def sentiment_analysis(text):
    # Get the sentiment score for the given text
    scores = analyzer.polarity_scores(text)

    # Determine the sentiment label based on the compound score
    compound_score = scores['compound']
    if compound_score >= 0.05:
        sentiment_label = "Positive"
    elif compound_score <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_label, scores

def main():
    st.title("Product Sentiment Analysis")

    # Input text from the user
    user_input = st.text_area("Enter your text:", "I love this product. It's amazing!")

    if st.button("Analyze Sentiment"):
        # Perform sentiment analysis
        sentiment, scores = sentiment_analysis(user_input)

        # Display the sentiment label and scores
        st.write("Sentiment Label:", sentiment)
        st.write("Sentiment Scores:", scores)

if __name__ == "__main__":
    main()
