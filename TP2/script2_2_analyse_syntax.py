import nltk
from nltk import word_tokenize,pos_tag

filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt'

fileout = filein+'.ne.nltk.'

with open(filein, 'r', newline='') as fsrc:
    text = fsrc.read()

tokens = word_tokenize(text)
tag=pos_tag(tokens)
#print(tag)

ne_tree = nltk.ne_chunk(tag)
print(ne_tree)