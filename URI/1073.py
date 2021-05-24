X = int(input())
Z = 0

for i in range(1, X+1):
  if i%2 == 0:
    print("%d^2 = %d" %(i, pow(i,2)))