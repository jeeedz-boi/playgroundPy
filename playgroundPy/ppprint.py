# 2[abc]3[ab]c output = abcabc ababab c
# 10[a]c2[ab] output = aaaaaaaaaa c abab
# 2[3[a]b] output = aaa b aaa 

arrayPrint = input('enter : ')
printList = list()
size = len(arrayPrint)
#print(arrayPrint)
def includeInList(check):
    numberList = ['1','2','3','4','5','6','7','8','9','0']
    for x in range(10):
        if(numberList[x] == check):
            return True
    return False

for x in range(size):

    if(arrayPrint[x]!='[' and includeInList(arrayPrint[x])):
        
        print('num found!')
    elif(arrayPrint[x]!='['):
        printList.append(arrayPrint[x])
        print('char found!')
    elif(arrayPrint[x]=='['):
        print('[ found!')


 