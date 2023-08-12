 # @mansourshebli 

# Tokenization with NLTK
# Imported the required libraries
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text for POS tagging demonstration
sample_text = "I am learning how to use POS tagging with NLTK."

# Tokenize the sample text into words
tokens = word_tokenize(sample_text)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

# Print the result
for word, pos_tag in pos_tags:
    print(f"Word: {word}, POS Tag: {pos_tag}")
