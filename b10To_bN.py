errorIn_b10TobN_typeError = "Error: maxNum or InNum invalid."
errorIn_b10TobN_BaceTooSmall = "Error: Base > 1 error or InNum is < 0."
errorIn_b10TobN_IDK_TBH = "Error: invalid N i think??"

def b10To_bN(InNum, N=10, maxMag=0):
    '''InNum is the number, N base number (real int only) and maxNum is the number of digits'''
    # edge cases
    if InNum == 0 :
        if N==1:
            return '1-1'
        return '0'
    if N < 1 or InNum < 0:
        return errorIn_b10TobN_BaceTooSmall
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
        maxMagUsed = dig #ceil(dig)
    else:
        maxMagUsed = maxMag

    # type prtecton
    if not(type(maxMagUsed) is int) and (type(InNum) is int):
        return errorIn_b10TobN_typeError
    # makes the output 
    outputStr = ''
    for i in range((maxMagUsed-1), -1, -1):
        mN = N**i
        if InNum < mN:
            outputStr += '0'
        else:
            if 10 > InNum//mN:
                outputStr += str(int(InNum//mN))
            else:
                try:
                    outputStr += chr(InNum//mN+65-10)
                except Exception:
                    return errorIn_b10TobN_IDK_TBH
            InNum = InNum % mN
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
    # print(b10To_bN(123,24.5))
    # # 50
    print(b10To_bN(int(input('input number:')),float(input('input base:'))))
