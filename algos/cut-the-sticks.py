n = int(raw_input())

lens = [int(x) for x in raw_input().split(" ")]

prev_len = len(lens)
print prev_len

while (len(lens) > 0):
    shortest = min(lens)
    for i in range(0,len(lens)):
        lens[i] = lens[i] - shortest
        
    lens = [item for item in lens if item > 0]
    new_len = len(lens)
    if new_len == 0:
        break
    print new_len
