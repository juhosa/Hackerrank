import math

T = int(raw_input())

for i in range (0,T):
    A,B = [int(x) for x in raw_input().split(" ")]

    a = math.ceil(math.sqrt(A))
    b = math.floor(math.sqrt(B))
    count = int(b-a+1)
    print count
    