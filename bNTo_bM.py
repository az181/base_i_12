import bNTo_b10
import b10To_bN

def bNTo_bM(bNNum,baseN=10,baseM=12,maxMag=0):
    '''base N to base M (where N and M are integers numbers) bNNum is a str (and the input number), Base is a value that can be converted to a complex number maxMag is an int (and the '''
    return b10To_bN.b10To_bN(bNTo_b10.bNTo_b10(bNNum,baseN,maxMag),baseM,maxMag)


if __name__=='__main__':
    # try:
        print(bNTo_bM(input('input the number to be comverted from base N to base M:'),
              complex(input('input the base N:')),complex(input('input the base M:'))))
    # except:
        print('Error: invalid input')