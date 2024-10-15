
#Word sense ambiguation
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize 

a1= lesk(word_tokenize('The building has a device to jam the signal'),'jam')
print(a1,a1.definition())
a2 = lesk(word_tokenize('I am stuck in a traffic jam'),'jam')
print(a2,a2.definition())

a1= lesk(word_tokenize('what is the current time ?'),'current')
print(a1,a1.definition())
a2 = lesk(word_tokenize('air current'),'current')
print(a2,a2.definition())



#Named Entity Recognition
nltk.download('maxent_ne_chunker')
nltk.download('words')


text = "Apple is an American company based out of California"
for w in nltk.word_tokenize(text):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(w))):
     if hasattr(chunk, 'label'):
        print(chunk.label(), ' '.join(c[0] for c in chunk))


text = "Narendra Modi is the Prime Minister of India"
for w in nltk.word_tokenize(text):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(w))):
     if hasattr(chunk, 'label'):
        print(chunk.label(), ' '.join(c[0] for c in chunk))  
