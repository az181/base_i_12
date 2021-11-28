
    
    
def inversi12(i12Num):
    i12Num='0'*(4-(len(i12Num)%4))+i12Num
    dig=len(i12Num)//4
    re=True
    b10Num=[0,0]
    print(i12Num)
    for x in enumerate(i12Num[::-1]):
        if (x[0]//4)>=2:
            re=False
        else:
            re=True
        if x[0]%2:
           b10Num[re]+=x[1]*12**(x[0]//4)
        
        