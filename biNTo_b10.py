#from bNTo_b10 import bNTo_b10

def biNTo_b10(biNNum, Base=12, maxMag=0):
    # error handling
    error=''
    if type(biNNum)!=str:
        error+='TypeError: invalid biNNum\n'
    if type(maxMag)!=int:
        error+='TypeError: invalid maxMag\n'
    if error!='':
        return error
    if Base == 0:
        return 'ZeroDivisionError: The base can not be 0'
    
    
    biNNum = '0'*(4-(len(biNNum) % 4))+biNNum
    im = False
    b10Num = [0, 0]
    
    # # not working get 
    # if Base ==1 and biNNum.count('1')==len(biNNum):
    #     for x in 
    #     if maxMag != 0:
    #         biNNum=str(biNNum.count('1'))
    #         return int(biNNum[len(biNNum)-maxMag:])
    #     else:
    #         return biNNum.count('1')
    
    # if Base == 10:
    #     if maxMag != 0:
    #         return int(biNNum[len(biNNum)-maxMag:])
    #     else:
    #         return int(biNNum)
    
    # the main program
    for x in enumerate(biNNum[::-1]):
        if x[1] == '0':
            im = not im
            continue
        if 49 <= ord(x[1]) <= 57:
            currntDig = int(x[1])
        elif 65<=ord(x[1]):
            currntDig = ord(x[1])-65+10
        # b10Num is list of [re,im] currntDig * Base**digitIndex *(1 if positive -1 if negative)
        b10Num[im] += currntDig*(Base**(x[0]//4))*(1-2*((x[0] % 4) >= 2))
        im = not im
    
    if maxMag != 0:
        for i in enumerate(b10Num):
            currntDig = str(i[1])
            b10Num[i[0]] = currntDig[len(currntDig)-maxMag:]
    for i in range(2):
        if b10Num[i]==int(b10Num[i]):
            b10Num[i]=int(b10Num[i])
    return complex(*b10Num)
        
        
if __name__=="__main__":
    # print(biNTo_b10('10032',5))
    # # (7+3j)
    # print(biNTo_b10('100020041009'))
    # # (57-169j)
    print(biNTo_b10(input('input base iN number:'),float(input('input the base:'))))