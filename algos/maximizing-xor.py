def  maxXor( l,  r):
  #return l^r
  lista = []
  for i in range(l,r+1):
      for j in range(i,r+1):         
          lista.append(i^j)
  
  return max(lista)

_l = int(raw_input());
#_l = 10;


_r = int(raw_input());
#_r = 15;

res = maxXor(_l, _r);
print(res)
