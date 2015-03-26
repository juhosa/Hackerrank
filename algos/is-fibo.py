fibs = [0,1]

while fibs[-1] <= 10**10:
    #print fibs[-2], fibs[-1]
    fibs.append(fibs[-2]+fibs[-1])
    
T = int(raw_input())

for _ in range(T):
    i = int(raw_input())
    if i in fibs:
        print 'IsFibo'
    else:
        print 'IsNotFibo'