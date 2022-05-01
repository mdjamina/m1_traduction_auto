
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from collections import Counter
from pprint import pprint as pp

import sys 


args = sys.argv[1:]


filein = args[0]


#filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt'

fileout = filein+'.ne.nltk'


with open(filein, 'r', newline='') as fsrc:
    text = fsrc.read()

tokens = word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

output = nltk.ne_chunk(pos_tags)  # POS tagging before chunking!

with open(fileout, 'w') as txtfile:
    for chk in output.subtrees(filter=lambda t: t.label() in  ['ORGANIZATION','PERSON','LOCATION','DATE','TIME','MONEY','PERCENT','FACILITY','GPE']):
           
            txtfile.write(chk.label() + '\t' + '\t'.join(['/'.join(list(l)) for l in chk.leaves()]))
            txtfile.write('\n')

