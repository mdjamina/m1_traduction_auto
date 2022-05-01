
import sys 


args = sys.argv[1:]

filein = args[0]

print(filein)
fileout = args[1]
print(fileout)
with open(fileout, 'w') as txtfile:
    
    with open(filein, 'r', newline='') as csvfile:
        
        for line in csvfile:
            row = line.split()    
            txtfile.write('_'.join(row))
            txtfile.write(' ')
            if row[0] == '.':
                txtfile.write('\n')

