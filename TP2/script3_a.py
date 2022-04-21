

"""

Remplacer à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers
« wsj_0010_sample.txt.pos.nltk » et 
« wsj_0010_sample.txt.pos.ref » par les
étiquettes universelles en utilisant la table de correspondance
« POSTags_PTB_Universal.txt »

"""


import sys 


args = sys.argv[1:]


file_POSTags = '/home/amina/workspace/github/m1_traduction_auto/TP2/POSTags_PTB_Universal_Linux.txt'
print(file_POSTags)



def load_univ_tags(path_file):
    uniTags = {}
    with open(path_file, 'r', newline='') as csvfile:        
        for line in csvfile:
            row = line.split()            
            key = row[0]
            value = row[1]
            uniTags[key] = value


    return uniTags

univ_tags = load_univ_tags(file_POSTags)

#print(univ_tags)



filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt.pos.ref'
fileout = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt.pos.univ.ref'
with open(fileout, 'w') as f_out: #écriture sur le fichier de sortie 
    
    with open(filein, 'r', newline='') as f_in:
        
        for line in f_in:
            for k,v in univ_tags.items():
                line = line.replace('_'+k+' ','_'+v+' ')
            
            print(line)
            
            f_out.write(line)

