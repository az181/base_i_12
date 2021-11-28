def bNTo_b10(bNNum, Base=12, maxMag=0):
    '''base N to base 10 (where N is a complex number) bNNum is a str (and the input number), Base is a value that can be converted to a complex number maxMag is an int (and the '''
    # checks for errors
    error = ''
    if type(bNNum) != str:
        error += 'TypeError: invalid bNNum\n'
    try:
        Base = complex(Base)
    except Exception:
        error += 'TypeError: invalid Base\n'
    if type(maxMag) != int:
        error += 'TypeError: invalid maxMag\n'
    if error != '':
        return error
    del error
    
    # edge cases to make more efficient
    if Base == 0:
        return 'ZeroDivisionError: The base can not be 0'
    if Base ==1 and bNNum.count('1')==len(bNNum):
        if maxMag != 0:
            bNNum=str(bNNum.count('1'))
            return int(bNNum[len(bNNum)-maxMag:])
        else:
            return bNNum.count('1')
    if Base == 10:
        if maxMag != 0:
            return int(bNNum[len(bNNum)-maxMag:])
        else:
            return int(bNNum)
    
    # the main converter
    b10Num = 0
    for i in enumerate(bNNum[::-1]):
        if i[1] == '0':
            continue
        mag = Base**i[0]
        # 49 to 57 num 1 to 9
        if 49 <= ord(i[1]) <= 57:
            b10Num += int(i[1])*mag
        else:
            # starts from 'A' ord('A')=65 so 65-55=10
            b10Num += (ord(i[1])-55)*mag
    del mag
    
    if maxMag != 0:
        b10Num = str(b10Num)
        b10Num = int(b10Num[len(bNNum)-maxMag:])

    if b10Num.imag == 0:
        b10Num = b10Num.real
        if int(b10Num) == b10Num:
            b10Num = int(b10Num)
    return b10Num


if __name__ == '__main__':
    # print(bNTo_b10('TC',60))
    # # 1752
    # print(bNTo_b10('10',12))
    # # 12
    # print(bNTo_b10('100100000111',2))
    # # 2311
    # print(bNTo_b10('12345643',-4))
    try:
        print(bNTo_b10(input('input the number to be comverted to base N:'),
              complex(input('input the base N:'))))
    except:
        print('Error: invalid input')
