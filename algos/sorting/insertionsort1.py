# this solution cannot be right.... but it works so who gives a damn.
def insertionSort(ar):    
    v = ar[-1]
    inserted = False
    for i in xrange(len(ar)-2,-1,-1):
        if ar[i] > v:
            ar[i+1] = ar[i]
            print ' '.join(map(str,ar))
        else:
            ar[i+1] = v
            inserted = True
            print ' '.join(map(str,ar))
            break
    if not inserted:
        ar[0] = v
        print ' '.join(map(str,ar))
        
        

m = int(raw_input())
ar = [int(i) for i in raw_input().split(" ")]
insertionSort(ar)