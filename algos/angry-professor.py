T = int(raw_input())

for i in range(0,T):
    n,k = [int(x) for x in raw_input().split(" ")]
    times = [int(x) for x in raw_input().split(" ")]
    
    times.sort() # this is prolly useless
    
    early_count = 0
    
    for i in times:
        if i <= 0:
            early_count += 1
        
    if early_count < k:
        print 'YES'
    else:
        print 'NO'        
    