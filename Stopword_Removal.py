# Import the NLTK library
import nltk

# Import specific modules and resources from NLTK
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary resources from NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Sample text for demonstration
sample_text = "Hello and welcome. This is a text for demonstrating how things work in stopwords!"

# Tokenize the sample text into words
token = word_tokenize(sample_text)

# Get the list of stopwords in English from NLTK
stop_words = set(stopwords.words('english'))

# Initialize an empty list to store tokenized words without stopwords
tokenized_words_without_stop_words = []

# Iterate through each word in the tokenized list
for word in token:
    # Check if the word is not a stopword
    if word not in stop_words:
        # If not a stopword, add it to the list of tokenized words without stopwords
        tokenized_words_without_stop_words.append(word)

# Print the list of tokenized words without stopwords
print(tokenized_words_without_stop_words)

