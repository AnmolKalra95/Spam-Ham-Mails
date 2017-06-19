import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
fileobj = open("Input.txt",'r')
sentence=fileobj.read()
stp_words=set(stopwords.words('english'))
token1 = tokenizer.tokenize(sentence)
filtered_sentence=[w for w in token1 if not w in stp_words]
print(filtered_sentence)
