import nltk

# nltk.download('punkt')

sentence = 'I am going to take the NLP class next semester'

tokens = nltk.word_tokenize(sentence)

i=0
for char in tokens:
	print(len(char))