#1)TOKENIZATION 
import nltk

nltk.download('punkt')

text = "Machine Learning is a Subset of Artificial intelligence, and it does with learning from data without being explicitly programmed"

ml_tokens = nltk.word_tokenize(text) 
print(ml_tokens)

#bigrams
print(list(nltk.bigrams(ml_tokens)))

#trigrams
print(list(nltk.trigrams(ml_tokens)))


#2)POS TAGGING
nltk.download("averaged_perceptron_tagger")

for token in ml_tokens:
  print(nltk.pos_tag([token]))


sent = "Jerry eats a banana"

tokens = nltk.word_tokenize(sent)
for token in tokens:
  print(nltk.pos_tag([token]))

#POS Using RegexpTokenizer
from nltk.tokenize import RegexpTokenizer  #import lib
reg_tokenizer = RegexpTokenizer('(?u)\W+|\$[\d\.]+|\S+') #Regex define and creating a new parameter
tokens = reg_tokenizer.tokenize(sent)
for token in tokens:
  print(nltk.pos_tag([token])) 

#Removing stop words
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


filtered_data = [w for w in ml_tokens if not w in stop_words]
print(filtered_data) 

