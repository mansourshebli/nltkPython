# @mansourshebli
import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Sample text for named entity recognition
sample_text = "Barack Obama was the 44th President of the United States. He was born in Hawaii."

# Tokenize the sample text into words
words = word_tokenize(sample_text)

# Perform named entity recognition
ner_result = ne_chunk(nltk.pos_tag(words))

# Print the named entity recognition result
print(ner_result)
