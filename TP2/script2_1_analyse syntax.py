

import nltk

from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from pprint import pprint as pp


with open("/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt") as fsrc:
    text = fsrc.read()

tokens = word_tokenize(text)



pos_tags = nltk.pos_tag(tokens)
#pp(pos_tags)


patterns= "NP: {<DT>?<JJ>*<NN>}"

chunker = RegexpParser(patterns)

print("After Regex:",chunker)


output = chunker.parse(pos_tags)
print("After Chunking",output)


#output.draw()
"""

grammar = "NP: {<DT>?<JJ>*<NN>}"

cp  =nltk.RegexpParser(grammar)

result = cp.parse(pos_tag)

print(result)

#result.draw()    # It will draw the pattern graphically which can be seen in Noun Phrase chunking 


"""