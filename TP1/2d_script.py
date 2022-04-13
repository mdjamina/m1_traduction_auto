
#
"""
Remplacer à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers
wsj_0010_sample.txt.pos.stanford et
wsj_0010_sample.pos.stanford.ref par les étiquettes universelles en utilisant
la table de correspondance « POSTags_PTB_Universal.txt ». Mettre le résultat de
2cette conversion dans les fichiers : wsj_0010_sample.txt.pos.univ.stanford
et wsj_0010_sample.txt.pos.univ.ref.

"""


import sys 


args = sys.argv[1:]


filein = args[0]
#print(filein)
fileout = args[1]
#rint(fileout)



def load_univ_tags(path_file):
    uniTags = {}
    with open(path_file, 'r', newline='') as csvfile:        
        for line in csvfile:
            row = line.split()            
            key = row[0]
            value = row[1]
            uniTags[key] = value


    return uniTags





univ_tags = load_univ_tags('/home/amina/workspace/github/m1_traduction_auto/TP1/POSTags_PTB_Universal_Linux.txt')



#print(univ_tags)
#filein = '/home/amina/workspace/github/m1_traduction_auto/TP1/wsj_0010_sample.txt.pos.stanford'
#fileout = '/home/amina/workspace/github/m1_traduction_auto/TP1/wsj_0010_sample.txt.pos.univ'
with open(fileout, 'w') as txtfile:
    
    with open(filein, 'r', newline='') as csvfile:
        
        for line in csvfile:
            for k,v in univ_tags.items():
                line = line.replace('_'+k+' ','_'+v+' ')
            
            #print(line)
            
            txtfile.write(line)
            
            
