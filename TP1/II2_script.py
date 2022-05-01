
from collections import defaultdict

def get_ner(lst):
    """"
       Méthode pour lister les entités nommées et leur fréquence
    """

    lst_ner = defaultdict(int)
    ner= ""
    ner_tagg = ""

    for token,tagg in lst_tokens:
    #print(tagg,token)    
        if tagg == 'O':        
            if ner!="":                
                lst_ner[tuple([ner.strip(),ner_tagg])]+=1     
            ner=""
        else:
            ner_tagg = tagg
            ner+=' '+token

    return lst_ner


filein = '/home/amina/workspace/github/m1_traduction_auto/TP1/wsj_0010_sample.txt.ner.stanford'
fileout = filein+'.output'
with open(filein, 'r', newline='') as fsrc:
    text = fsrc.read()



lst_tokens = [tuple(token.split('/')) for token in  text.split()]

lst_ner = get_ner(lst_tokens)

nb_occ_ner = sum(lst_ner.values())

with open(fileout,'w') as fcsv:
    for ner,occ in lst_ner.items():

        print(ner[0],'|',ner[1],'|',occ,'|', occ/nb_occ_ner,f'({occ}/{nb_occ_ner})')
        fcsv.write('{0}|{1}|{2}|{3} ({4}/{5})\n'.format(ner[0],ner[1],occ, occ/nb_occ_ner,occ,nb_occ_ner))



