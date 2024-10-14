#Stemming

from nltk.stem import PorterStemmer 

porter = PorterStemmer()
words = ['generous', 'generate','genorously', 'generation']
for word in words:
  print(f"{word} --> {porter.stem(word)}") 
