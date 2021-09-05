#STOPWORDS => Use Corpos Terminology

# It is use to remove the stopwords from sentence
# the stopwords like is, the, this, with a



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

sample_sentence = "Hello! this is Tokenization Method with the people"
a = word_tokenize(sample_sentence)


print(a)

for word in a:
    if word not in stop_words:
        print(word)