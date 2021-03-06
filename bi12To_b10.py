def bi12To_b10(i12Num, maxMag=0):
    # error handling
    error=''
    if type(i12Num)!=str:
        error+='TypeError: invalid i12Num\n'
    if type(maxMag)!=int:
        error+='TypeError: invalid maxMag\n'
    if error!='':
        return error
    
    
    i12Num = '0'*(4-(len(i12Num) % 4))+i12Num
    im = False
    b10Num = [0, 0]
    num = [str(i) for i in range(1,10)]

    for x in enumerate(i12Num[::-1]):
        if x[1] == '0':
            im = not im
            continue
        if x[1] in num:
            currntDig = int(x[1])
        else:
            currntDig = ord(x[1])-65+10
        # b10Num is list of [re,im] currntDig * 12**n *(1 if positive -1 if negative)
        b10Num[im] += currntDig*(12**(x[0]//4))*(1-2*((x[0] % 4) >= 2))
        im = not im

    if maxMag != 0:
        for i in enumerate(b10Num):
            currntDig = str(i[1])
            b10Num[i[0]] = currntDig[len(currntDig)-maxMag:]
    return complex(*b10Num)


if __name__ == '__main__':
    # print(bi12To_b10('100020041009'))
    # # (57-169j)
    # print(bi12To_b10('3004900B'))
    # # (59-45j)
    # print(bi12To_b10('100BB00'))
    # # (-23-11j)
    # print(bi12To_b10('1234'))
    # # (2+2j)
    print(bi12To_b10(input('input basei12 number:')))