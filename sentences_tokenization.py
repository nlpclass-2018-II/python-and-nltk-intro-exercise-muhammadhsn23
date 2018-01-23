import nltk

# nltk.download('punkt')

#English File
file = open('number7.txt')
sentences = file.read()
#Bahasa Indonesia File
file = open('balon.txt')
sentences2 = file.read()

sent_text = nltk.sent_tokenize(sentences)

file = open('results.txt', 'w')

i=1
for sentence in sent_text: #iterate through all splitted words
	print(i, sentence) #print the number of characters in the words
	file.write(sentence) #write each sentence on file results.txt
	i+=1