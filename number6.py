import nltk

# nltk.download('punkt')

sentence = 'I am going to take the NLP class next semester'

tokens = nltk.word_tokenize(sentence)

i=0
for words in tokens: #iterate through all splitted words
	print(len(words)) #print the number of characters in the words