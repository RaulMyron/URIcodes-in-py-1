A, B = map(int, input().split())

if(A == 0 and (B == 0 or B == 1)):
  print("C")
elif(A == 1 and B == 0):
  print("B")
elif(A == 1 and B == 1):
  print("A")