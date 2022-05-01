
import sys 


args = sys.argv[1:]


filein = args[0]

#filein = '/home/amina/workspace/github/m1_traduction_auto/TP2/wsj_0010_sample.txt.ne.standard'

fileout = filein.replace('.standard','.bio')


with open(filein, 'r', newline='') as fsrc:
    with open(fileout, 'w') as txtfile: 
        for line in fsrc:
            row = line.split()
            for i,c in enumerate(row[1:]):
                tag = 'I-' + row[0]
                token = c.split('/')[0]
                if i == 0:
                    tag = 'B-' + row[0]
                txtfile.write(f'{token}\t{tag}\n')
                




