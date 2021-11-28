from b10To_bN import b10To_bN


def b10To_biN(b10Comp, N=12, maxMag=0):
    '''b10Comp is type complex (int works too), N is the real part of the base maxMag is the number of digits'''
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
        temp = N
        while temp > 1:
            temp = maxMag/(N**dig)
            dig += 1
        maxMag = dig

    # converts real and imaginary to base N
    bNRe = b10To_bN(b10ReAbs, N, maxMag)
    bNIm = b10To_bN(b10ImAbs, N, maxMag)
    b_iN = ''
    if ('Error: invalid maxNum' in bNRe) or ('Error: invalid maxNum' in bNIm):
        return 'invalid maxMag'
    # puts the real and imag in the i subscript N base
    for x in range(maxMag*4):
        x4 = x % 4
        if x4 % 2 == 0 and (((not Im) and x4 == 0) ^ (Im and x4 == 2)):
            b_iN += bNIm[x//4]
        elif (((not Re) and x4 == 1) ^ (Re and x4 == 3)):
            b_iN += bNRe[x//4]
        else:
            b_iN += '0'
    for i in b_iN:
        if i == '0':
            b_iN = b_iN[1:]
        else:
            return b_iN


if __name__ == '__main__':
    print(b10To_biN(7+3J, 5))
