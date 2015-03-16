def work(jar_count,op_count,ops):
    total = 0        
    for op in ops:
        tmp = op.split(" ")
        total = total + (int(tmp[1]) - int(tmp[0]) + 1) * int(tmp[2])
    return total/jar_count


first_line = raw_input()

jars = int(first_line.split(" ")[0])
op_count = int(first_line.split(" ")[1])

opslist = []
for _ in xrange(0,op_count):
    tmp = raw_input()
    opslist.append(tmp)

answer = work(jars,op_count,opslist)
print answer