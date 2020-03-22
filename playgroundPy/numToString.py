import time

unitAsString = {
    '1' : 'หนึ่ง',
    '2' : 'สอง',
    '3' : 'สาม',
    '4' : 'สี่',
    '5' : 'ห้า',
    '6' : 'หก',
    '7' : 'เจ็ด',
    '8' : 'แปด',
    '9' : 'เก้า',
    '0' : ''   
}
expAsString = {
    '1' : '',
    '2' : 'สิบ',
    '3' : 'ร้อย',
    '4' : 'พัน',
    '5' : 'หมื่น',
    '6' : 'แสน',
    '7' : 'ล้าน'  
}

def convertToString(numList):
    result = list()
    unit = 1
    for x in numList: 
        if(x=='0'):
            print(end='')
        elif (unit == 1 and len(numList) > 1 and x == '1'):
            result.append('เอ็ด'+expAsString[str(unit)])
        elif (unit == 2 and x == '2'):
            result.append('ยี่'+expAsString[str(unit)])
        elif (unit == 2 and x == '1'):
            result.append('สิบ')
        else : 
            result.append(unitAsString[x]+expAsString[str(unit)])
        unit = unit + 1

        if(unit == 7):
            unit = 1
            result.append('ล้าน')
    return result

def NTS():
    step = 0
    num = input('What your number : ')
    if(num=='e' or num=='ex' or num=='exit'):
        print('Good bye have a good day!')
        return False
    
    print(f"{int(num):,}")

    print('Coverting')
    while(step < 5):
        print(' . ')
        step = step + 1
        time.sleep(0.5)
    numList = list(num)
    # print('list(num)',numList)
    # result = convertToString(list(reversed(numList)))
    # prettyPrint(list(reversed(convertToString(list(reversed(numList)))))) # worked!
    print('=> ',end='')
    print (''.join(list(reversed(convertToString(list(reversed(numList)))))))
    return True 
        
if __name__ == "__main__":
    running = True
    while(running):
        running = NTS()