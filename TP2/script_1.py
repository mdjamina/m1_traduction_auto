
import sys
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from collections import Counter
from pprint import pprint as pp






filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt'

fileout = filein+'.pos.nltk2'


with open(filein, 'r', newline='') as fsrc:
    text = fsrc.read()

tokens = word_tokenize(text)



pos_tags = nltk.pos_tag(tokens)
#pp(pos_tags)

with open(fileout, 'w') as txtfile:
    for token_pos in pos_tags:
        txtfile.write('\t'.join(token_pos))
        txtfile.write('\n')
        #if token_pos[0] == '.':
         #   txtfile.write('\n')

