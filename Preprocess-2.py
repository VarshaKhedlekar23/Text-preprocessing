#Stemming- converting into root form
from nltk.stem import PorterStemmer 

porter = PorterStemmer()
words = ['generous', 'generate','genorously', 'generation']
for word in words:
  print(f"{word} --> {porter.stem(word)}") 


from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language='english')
words = ['generous', 'generate','genorously', 'generation']
for word in words:
  print(f"{word} --> {snowball.stem(word)}")


from nltk.stem import LancasterStemmer

lan = LancasterStemmer()
words = ['generous', 'generate','genorously', 'generation']
for word in words:
  print(f"{word} --> {lan.stem(word)}")


from nltk.stem import RegexpStemmer

reg = RegexpStemmer('ing|s$|ables$',min=4)
words = ['generous', 'generate','genorously', 'generation']
for word in words:
  print(f"{word} --> {reg.stem(word)}")



#Lemmmatization- converting into root form with context
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4') 

lemma = WordNetLemmatizer()
for word in words:
  print(f"{word} --> {lemma.lemmatize(word)}")



