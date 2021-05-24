X = int(input())
Y = int(input())
Z = 0

for i in range(Y+1, X):
  if i%2 != 0:
    Z += i
    
print(Z)