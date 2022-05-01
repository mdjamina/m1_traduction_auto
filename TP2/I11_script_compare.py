
import sys 
from pprint import pprint as pp

args = sys.argv[1:]


#file_ref = args[0]

file_ref = "/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.pos.ref" #fichier de reference
print(file_ref)
file_nltk = "/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt.pos.nltk" # fichier pos_nltk
print(file_ref)
with open(file_ref, 'r') as fref:
    ltokens_ref = [tuple(line.split()) for line in fref.readlines() if line.split() !=[]] #lire et spliter fref
    
pp(ltokens_ref) # afffichage une liste de tuples token, pos

with open(file_nltk, 'r') as fnltk:
    
    ltokens_nltk = [tuple(token.split('_')) for token in fnltk.read().split()] # lire et spliter fnltk
    
pp(ltokens_nltk)

for nltk,ref in zip(ltokens_nltk,ltokens_ref): # liste de tuples token et tag_ref
   
        print(ref,nltk)

