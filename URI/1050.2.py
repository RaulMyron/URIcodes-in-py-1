def verificaCIDADE(a):
  DDD=[61, 71, 11, 21, 32, 19, 27, 31]
  DDDcidades=["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
  cidade = 0
  for i in range(8):
    if(x==DDD[i]):
      cidade = DDDcidades[i]
    
  return cidade

x = int(input())

y = verificaCIDADE(x)
if(y != 0):
  print(y)
else:
  print("DDD nao cadastrado")
