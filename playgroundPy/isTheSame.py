from pprint import pprint

fileRead = open('Relabel_needed.txt','r')
relabel = list()
relabelNeeded = list()
same = list()

for line in fileRead:
    jpgName = line.split('.')
    if(len(jpgName[1].strip()) <= 3):
        relabel.append(jpgName[0])
    
relabel.sort()

x = 0
lastnotSame = True

print(len(relabel))
while(x < len(relabel) - 1):
    if (relabel[x] == relabel[x+1]):
        print('SAME! : ',relabel[x])
        lastnotSame = False
        same.append(relabel[x])
    else :
        relabelNeeded.append(relabel[x])   
    x = x + 1
    if (x==len(relabel)-1 and lastnotSame):
        relabelNeeded.append(relabel[x]) 

pprint(relabelNeeded)
print('\nRelabel needed amount ::',len(relabelNeeded))
if(lastnotSame):
    print('There is no same in this file')
else:
    print('There is same show in this list :')
    pprint(same)