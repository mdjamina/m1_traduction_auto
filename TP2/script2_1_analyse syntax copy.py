

from textwrap import indent
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from pprint import pprint as pp


filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt'

fileout = filein+'.chk.nltk'


with open("/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt") as fsrc:
    text = fsrc.read()

tokens = word_tokenize(text)



pos_tags = nltk.pos_tag(tokens)
#pp(pos_tags)


#grammar ="Compound: {<DT>?<JJ>*<NN>}"

#Généralisation du programme 2.1 pour avoir les structures syntaxiques suivantes "Adjectif-Nom","Nom-Nom","Adjectif-Nom-Nom","Adjectif-Adjectif-Nom"
# On ajoute + dans notre REgex grammar ="Compound: {<DT>?<JJ>*<NN>+}"
grammar ="Compound: {<DT>?<JJ>*<NN>+}"
"""
grammar = '\n'.join([
	'Determinant-Adjectif-Nom: {<DT><JJ><NN>}',
	'Determinant-Nom: {<DT><NN>}',
	'Adjectif-Nom: {<JJ><NN>}',
	'Nom-Nom: {<NN><NN>}',
	'Adjectif-Nom-Nom: {<JJ><NN><NN>}',
	'Adjectif-Adjectif-Nom: {<JJ><JJ><NN>}',
	])
"""
chunker = RegexpParser(grammar)

print("After Regex:",chunker)


output = chunker.parse(pos_tags)
#print("After Chunking",type(output))



with open(fileout, 'w') as txtfile:
    for chk in output.subtrees(filter=lambda t: t.label() in ['Determinant-Nom','Determinant-Adjectif-Nom','Adjectif-Nom','Nom-Nom','Adjectif-Nom-Nom','Adjectif-Adjectif-Nom']):
        txtfile.write(chk.pformat())
        txtfile.write('\n')

