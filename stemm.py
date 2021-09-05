#Stemming

# Stemming is use to convert the same kind of words into
# one single words from the sentence
# for ex. [print, printing, printed, prints]
# converted is: [print]

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

port = PorterStemmer()
sample = "He eats what he was eating yesterday at the eatery"

for word in word_tokenize(sample):
    print(port.stem(word))