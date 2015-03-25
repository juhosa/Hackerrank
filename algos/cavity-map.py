n = int(raw_input())

maps = []

for i in xrange(n):
    maps.append([int(x) for x in raw_input()])

length_is_one = False
if len(maps) == 1:
    print maps[0][0]
    length_is_one = True
    

if length_is_one is False:    
    print ''.join(map(str,maps[0]))
    for i in xrange(1, len(maps)-1):
        line = ''
        line += str(maps[i][0])
        for j in xrange(1,len(maps[0])-1):
            current = maps[i][j]

            up = maps[i-1][j]

            left = maps[i][j-1]
            ri = maps[i][j+1]

            down = maps[i+1][j]

            if up < current and left < current and ri < current and down < current:
                line += 'X'
            else:
                line += str(current)
            
        line += str(maps[i][-1])        
        print line
    print ''.join(map(str,maps[-1]))
            
            
            
            
            
            
            
            
            
            
