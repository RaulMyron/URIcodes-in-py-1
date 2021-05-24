C1, C2, C3 = map(int, input().split())

if(C1==C2 or C1==C3):
  print("S")
elif(C2==C3 or C2==C1):
  print("S")
elif(C3==C2 or C3==C1):
  print("S")
elif(C1+C2==C3):
  print("S")
elif(C2+C3==C1):
  print("S")
elif(C1+C3==C2):
  print("S")
else:
  print("N")