n,T = [int(x) for x in raw_input().split(" ")]

widths = [int(x) for x in raw_input().split(" ")]

for test in range(0,T):
    i,j = [int(x) for x in raw_input().split(" ")]
    
    smallest = 999999
    
    for segment in range(i,j+1):
        if widths[segment] < smallest:
            smallest = widths[segment]
    
    print smallest
    