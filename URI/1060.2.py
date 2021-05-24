a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

contador = 0

for i in (a, b, c, d, e, f):
  if(i>0):
    contador += 1

print(contador, "valores positivos")