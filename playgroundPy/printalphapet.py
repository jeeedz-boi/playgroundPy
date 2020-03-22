# inp1 = 2[abc]3[ab]c
# out1 = abcabcabababc  
# inp2 = 10[a]c2[ab]
# out2 = aaaaaaaaaacabab
# inp3 = 2[3[a]b]
# out3 = aaabaaab

def split(words):
    return [char for char in words]

def findN(list,count):
    print()

def findC(list):
    lenght = 0
    i = 0
    while i < len(list):
        if isinstance(list[lenght],str) and list[lenght]!="0" and list[lenght]!="1" and list[lenght]!="2" and list[lenght]!="3" and list[lenght]!="4" and list[lenght]!="5" and list[lenght]!="6" and list[lenght]!="7" and list[lenght]!="8" and list[lenght]!="9":
            print(list[lenght])
        else :
            print()
        i = i + 1
        lenght = lenght + 1


x = "string"
while x != "stop" :
    x = input()
    if x == "stop":
         break
    findC(split(x))