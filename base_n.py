def bNCom(InNum, N=10, maxMag=0):
    '''InNum is the number, N base number (real int only) and maxNum is the number of digits'''
    if N==10:
        if not maxMag == 0:
            return InNum[len(InNum)-maxMag:]
        return InNum
    if maxMag == 0:
        maxMagUsed = InNum
        dig = 0
        temp = N
        while temp > 1:
            temp = maxMagUsed/(N**dig)
            dig += 1
        maxMagUsed= dig
    else:
        maxMagUsed = maxMag

    if not(type(maxMagUsed) is int) and (type(InNum) is int):
        return'maxNum or InNum invalid'
    baseNList = []
    for i in range((maxMagUsed-1), -1, -1):
        mN = N**i
        if InNum < mN:
            baseNList.append('0')
        else:
            if 10 > InNum//mN:
                baseNList.append(str(int(InNum//mN)))
            elif 10 <= InNum//mN:
                try:
                    baseNList.append(chr(InNum//mN+65-10))
                except Exception:
                    return '#invalid N i think??'
            else:
                return '#invalid maxNum ???'
            InNum = InNum % mN
    outputStr = ''
    for i in baseNList:
        outputStr += i
    if not maxMag == 0:
        outputStr = outputStr[len(outputStr)-maxMag:]
    else:
        for i in outputStr:
            if i=='0':
                outputStr = outputStr[1:]
            else:
                break
    return outputStr

if __name__=='__main__':
    print(bNCom(36,37))
    print(bNCom(1752,57))
    print(bNCom(857621339472816227,60))
