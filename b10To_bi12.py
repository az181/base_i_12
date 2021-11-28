def b10To_b12(InNum, maxMag):
    '''InNum is the number and maxNum is the number of digits'''
    if not(type(maxMag) is int) and (type(InNum) is int):
        return'maxNum or InNum invalid'
    base12List = []
    for i in range((maxMag-1), -1, -1):
        m12 = 12**i
        if InNum < m12:
            base12List+='0'
        else:
            if 10 > InNum//m12:
                base12List+=str(int(InNum//m12))
            elif 10 <= InNum//m12:
                try:
                    base12List+=chr(InNum//m12+65-10)
                except KeyError:
                    return 'Error: invalid maxNum'
            else:
                return 'Error: invalid maxNum'
            InNum = InNum % m12
    outputStr = ''
    for i in base12List:
        outputStr += i
    return outputStr


def b10To_bi12(b10Comp, maxMag=0):
    '''b10Comp is type complex (int works too), maxMag is the number of digits'''
    try:
        b10ReAbs = abs(b10Comp.real)
        b10ImAbs = abs(b10Comp.imag)
    except:
        return 'invalid input'

    Re = True
    Im = True
    # positive or negative real
    if b10ReAbs != b10Comp.real:
        Re = False
    # positive or negative imaginary
    if b10ImAbs != b10Comp.imag:
        Im = False

    if maxMag == 0:
        # finds the bigset one
        if b10ReAbs >= b10ImAbs:
            maxMag = b10ReAbs
        else:
            maxMag = b10ImAbs
        dig = 0
        temp = 12
        while temp > 1:
            temp = maxMag/(12**dig)
            dig += 1
        maxMag = dig

    # converts real and imaginary to base 12
    b12Re = b10To_b12(b10ReAbs, maxMag)
    b12Im = b10To_b12(b10ImAbs, maxMag)
    b_i12 = ''
    if ('Error: invalid maxNum' in b12Re) or ('Error: invalid maxNum' in b12Im):
        return 'Error: invalid maxMag'
    # puts the real and imag in the i subscript 12 base
    for x in range(maxMag*4):
        x4 = x % 4
        if x4 % 2 == 0 and (((not Im) and x4 == 0) ^ (Im and x4 == 2)):
            b_i12 += b12Im[x//4]
        elif (((not Re) and x4 == 1) ^ (Re and x4 == 3)):
            b_i12 += b12Re[x//4]
        else:
            b_i12 += '0'
    for i in b_i12:
        if i == '0':
            b_i12 = b_i12[1:]
        else:
            return b_i12


if __name__ == '__main__':
    # print(b102b12(12, 2))
    # # '10'
    # print(b102bi12(57-169j))
    # # '100020041009'
    # print(b102bi12(12+12j, 1))
    # # 'Error: invalid maxMag'
    print(b10To_bi12(complex(input('input complex number here:'))))