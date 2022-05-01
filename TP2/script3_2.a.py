

import sys 


args = sys.argv[1:]


filein = args[0]

#filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt.ne.nltk'

fileout = filein.replace('.nltk','.standard')


with open(filein, 'r', newline='') as fsrc:
    with open(fileout, 'w') as txtfile: 
        for line in fsrc:
            for tag in [('ORGANIZATION','ORG'),('PERSON','PERS'),('LOCATION','LOC'),('DATE','MISC'),('TIME','MISC'),('MONEY','MISC'),('PERCENT','MISC'),('FACILITY','ORG'),('GPE','LOC')]:
                line = line.replace(tag[0],tag[1])
            txtfile.write(line)



