M = int(input())
A = int(input())
B = int(input())

C = -(A + B - M)

maisvelho = 0

if(C>A and C>B):
  maisvelho = C
elif(A>B and A>C):
  maisvelho = A
else:
  maisvelho = B

print(maisvelho)