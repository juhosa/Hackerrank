T = int(raw_input())

for i in range(0,T):
    stones = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    
    if a > b:
        tmp = a
        a = b
        b = tmp
    
    min = (stones-1)*a
    max = (stones-1)*b
    ret = []
    step = b-a
    if step == 0:
        step = 1
        
    for i in range(min,max+1,(step)):
        ret.append(i)
        
    ret.sort()

    retstr = ''
    for i,n in enumerate(ret):
        if i != 0:
            retstr = retstr + ' ' + str(n)
        else:
            retstr = retstr + str(n)
            
    print retstr