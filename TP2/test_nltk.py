from distutils import core
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from collections import Counter

#test
text = "It’s works!"
print(word_tokenize(text))

#nltk.pos_tag(text)

"""
1.1. Ecrire un programme Python utilisant le package pos_tag pour désambiguïser morpho-
syntaxiquement le texte du fichier wsj_0010_sample.txt. Le résultat de ce module sera 
mis dans le fichier wsj_0010_sample.txt.pos.nltk

"""


with open ("TP 2/wsj_0010_sample.txt","r") as fsrc:

    corpus= fsrc.read()
    #print(word_tokenize(corpus))

    print(pos_tag(word_tokenize(corpus)), "\n" , "===================================== ")

    tokens = nltk.wordpunct_tokenize(corpus)
    tags = nltk.pos_tag(tokens)
    counts = Counter (tag for word, tag in tags)
    print(counts)
