from math import log , ceil, log1p
from sre_constants import MAXGROUPS 

errorInb10To_b12_mAndI = "Error: maxNum or InNum invalid (in b10To_b12)"
errorInb10To_b12_mRange = "Error: invalid maxMag (in b10To_b12)"
errorInb10To_bi12_input = "Error: invalid input (in b10To_bi12)"
errorInb10To_bi12_magBad = "Error: invalid maxMag (in b10To_bi12)"

def b10To_b12(InNum, maxMag, inproper=False):
    '''InNum is the number and maxNum is the number of digits'''
    if not((type(maxMag) is int) and (type(InNum) is int)):
        return errorInb10To_b12_mAndI
    base12List = ""
    for i in range((maxMag-1), -1, -1):
        m12 = 12**i
        if InNum < m12:
            base12List+='0'
        else:
            if 10 > InNum//m12:
                base12List+=str(int(InNum//m12))
            elif 10 <= InNum//m12 < 12+inproper*InNum:
                base12List+=chr(InNum//m12+65-10)
            else:
                return errorInb10To_b12_mRange
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
        return errorInb10To_bi12_input

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
        maxMag = ceil( log(maxMag,12))+1

    # converts real and imaginary to base 12
    b12Re = b10To_b12(int(b10ReAbs), maxMag)
    b12Im = b10To_b12(int(b10ImAbs), maxMag)
    b_i12 = ''
    if (errorInb10To_b12_mRange in b12Re) or (errorInb10To_b12_mRange in b12Im):
        return errorInb10To_bi12_magBad
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
    print(b10To_b12(12, 2))
    # '10'
    print(b10To_b12(12330,4))
    # '7176'
    print(b10To_bi12(57-169j))
    # '100020041009'
    print(b10To_b12(40012,4,1))
    print(b10To_bi12(12+12j, 1))
    # 'Error: invalid maxMag (in b10To_bi12)'
    print(b10To_bi12(complex(input('input complex number here:'))))