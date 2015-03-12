t = int(raw_input())

if t is 0:
    print 1

cycles = []
for i in range(0,t):
    cycles.append(int(raw_input()))
    
for c in cycles:
    h = 1
    for i in range(0,c):
        if i % 2 == 0:
            h = h * 2
        else:
            h = h + 1
    print h
