t = int(raw_input())

for i in range(0,t):
    n = raw_input()
    n_list = list(n)
    
    count = 0
    
    for i in n_list:
        if int(i) == 0:
            continue
        elif int(n) % int(i) == 0:
            count += 1
            
    print count
            
    