
import nltk

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize 

sentence="The National Association of Manufacturers settled on the Hoosier capital of Indianapolis for its fall board meeting."

for sent in nltk.sent_tokenize(sentence):
   for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      if hasattr(chunk, 'label'):
         print(chunk.label(), ' '.join(c[0] for c in chunk))