# @mansourshebli 

# Tokenization with NLTK
# Imported the required libraries
import nltk
import matplotlib.pyplot as plt

# Download the necessary data for tokenization (if not already downloaded)
nltk.download('punkt')

# Sample text for tokenization
sample_text = "Hello and welcome. This is a sample text for demonstration."

# Importing the word_tokenize and sent_tokenize functions from the NLTK library
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
# Also importing the FreqDist function from the NLTK library (probability module) :)
from nltk.probability import FreqDist

# Tokenize the text into words using word_tokenize
token = word_tokenize(sample_text)

# Tokenize the text into sentences using sent_tokenize
senToken = sent_tokenize(sample_text)

# Create a frequency distribution of characters in the sample text using FreqDist
fd = FreqDist(sample_text)

# Plot the frequency distribution of characters (top 30) using FreqDist.plot()
fd.plot(30, cumulative=False)
plt.show()

# Print the three most common characters and their frequencies
print(fd.most_common(3))

# Print the tokenized sentences
print(senToken)

# Print the tokenized words
print(token)

# Print the frequency distribution of characters
print(fd)

