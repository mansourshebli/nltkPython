# @mansourshebli

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary resources
nltk.download('vader_lexicon')

# Initialize the VADER sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
sample_text = "I love this product! It's so amazing and useful."

# Perform sentiment analysis
sentiment_scores = sia.polarity_scores(sample_text)

# Interpret the sentiment scores
if sentiment_scores['compound'] >= 0.05:
    sentiment = "positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "negative"
else:
    sentiment = "neutral"

# Print the sentiment analysis result
print(f"Sample Text: {sample_text}")
print(f"Sentiment: {sentiment}")
print("Sentiment Scores:", sentiment_scores)
