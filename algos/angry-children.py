def angry2(n,k,nums):
    smallest = None
 
    for i in xrange(0,n):
        tmp = nums[i:k+i:k-1]
        
        if len(tmp) < 2:
            break
        
        f = tmp[1] - tmp[0]
        
        if smallest is None or f < smallest:
            smallest = f
    
    return smallest

N = int(raw_input())
K = int(raw_input())

lists = [int(raw_input()) for _ in range(0,N)]

lists.sort()

min_diff = angry2(N,K,lists)

print min_diff