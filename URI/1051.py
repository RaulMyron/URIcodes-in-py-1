x = float(input())
y = 0
if(x>0 and x<=2000):
  print("Isento")
elif(x>2000 and x<=3000):
  y=0.08
  print("R$ %.2f" %((x-2000)*y))
elif(x>3000 and x<=4500):
  y=0.18
  print("R$ %.2f" %((x-3000)*0.18+ (1000*0.08)))
else:
  y=0.28
  print("R$ %.2f" %((x-4500)*0.28+(1500*0.18)+(1000*0.08)))