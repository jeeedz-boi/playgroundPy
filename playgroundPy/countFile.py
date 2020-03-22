def counting() : 
    fileRead = open("Labeled.txt", "r")
    while True : 
        foundEh = True
        amout = 0
        date = input('What date do you like to know how much I lebeling? (dd/mm/yyyy): ')
        if date != 'exit': 
            for F in fileRead:
            
                if not foundEh:
                    if len(F) > 5 :
                        break
                    amout = amout + 1
                    
                if len(F) > 5 and foundEh: 
                    temp = F.split('+')
                    if temp[1] == date:
                        print(temp[1]+' FOUND IT!!')
                        foundEh = False
                    else :
                        print('NOPE!!')
        else : 
            print('Bye~')
            return 0
        if foundEh:
            print('This date I had not lebeling at all!')
        elif not foundEh :
            print('In date ' +str(date) + ' I had lebeling for : ' +str(amout+1) )
        fileRead.seek(0) # re-read file 

if __name__ == "__main__":
    counting()