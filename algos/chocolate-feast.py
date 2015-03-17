T = int(raw_input())

for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    
    vals = []
    a = A/B
    vals.append(a)
    b = (a/C1)
    vals.append(b)
    tmp = 1000000000000
    index = 0
    while tmp > C1:
        tmp = (vals[index+1] + (vals[index]%C1))/C1
        vals.append(tmp)
        index += 1

    answer = sum(vals)
    print answer