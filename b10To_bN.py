def b10To_bN(InNum, N=10, maxMag=0):
    '''InNum is the number, N base number (real int only) and maxNum is the number of digits'''
    if N == 10:
        if not maxMag == 0:
            InNum = str(InNum)
            InNum = '0'*(maxMag-len(InNum))+InNum[len(InNum)-maxMag:]
            return InNum
        return str(InNum)
    if N==1:
        outputStr=InNum*'1'
        if outputStr=='':
            outputStr='0'
        return outputStr
    
    if maxMag == 0:
        maxMagUsed = InNum
        dig = 0
        temp = N
        while temp > 1:
            temp = maxMagUsed/(N**dig)
            dig += 1
        maxMagUsed = dig
    else:
        maxMagUsed = maxMag

    if not(type(maxMagUsed) is int) and (type(InNum) is int):
        return'maxNum or InNum invalid'
    outputStr = ''
    for i in range((maxMagUsed-1), -1, -1):
        mN = N**i
        if InNum < mN:
            outputStr += '0'
        else:
            if 10 > InNum//mN:
                outputStr += str(int(InNum//mN))
            elif 10 <= InNum//mN:
                try:
                    outputStr += chr(InNum//mN+65-10)
                except Exception:
                    return 'Error: invalid N i think??'
            else:
                return 'Error: invalid maxNum ???'
            InNum = InNum % mN
    # for i in outputStr:
    #     outputStr += i
    if maxMag != 0:
        outputStr = outputStr[len(outputStr)-maxMag:]
    else:
        for i in outputStr:
            if i == '0':
                outputStr = outputStr[1:]
            else:
                break
    return outputStr


if __name__ == '__main__':
    # print(b10To_bN(36, 10, 5))
    # # 00036
    # print(b10To_bN(36, 37, 3))
    # # 00[
    # print(b10To_bN(1752, 60))
    # # TC
    # print(b10To_bN(857621339472816227, 60))
    # # 1P63L`AQ03f
    print(b10To_bN(int(input('input number:')),int(input('input base:'))))
