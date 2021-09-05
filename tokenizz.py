from nltk.tokenize import word_tokenize, sent_tokenize

sample_sentence = "Hello! this is Tokenization Method"

a = word_tokenize(sample_sentence)
print(a)

b = sent_tokenize(sample_sentence)
print(b)
