
#
from re import S


import sys 


args = sys.argv[1:]

 #chemin du fichier de l'entrée
filein = args[0] 
#print(filein)

#chemin du fichier de la sortie
fileout = args[1] 
#rint(fileout)



def load_univ_tags(path_file):  
    """Méthode pour charger l'univ tags
    """

    #Initialiser le dictionnaire uniTags pour stocker les tags
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
            
            
#on a baissé le score de la précision sur les tags