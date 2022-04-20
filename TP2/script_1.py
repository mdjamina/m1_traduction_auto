
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from collections import Counter
from pprint import pprint as pp






filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt'
with open(filein, 'r', newline='') as fsrc:
    text = fsrc.read()

tokens = nltk.wordpunct_tokenize(text)



pos_tags = nltk.pos_tag(tokens)
pp(pos_tags)

#for token_pos in pos_tags:

    #print(token,pos)


