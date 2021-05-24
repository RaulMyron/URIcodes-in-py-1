litros = int(input())

qtdmax = litros

comando = 0
km = 0
passou = True
negativos = []

while(comando!=-1):

  comando = int(input())

  if(comando!=-1 and litros!=0):
    if(comando==0):
      litros-=1
      km+=1
    elif(comando==1):
      litros+=int(input())
      km+=1
      if(litros>=qtdmax):
        litros=qtdmax
    elif(comando==2):
      litros-=int(input())
      km+=1
      if(litros<=0):
        passou = False
        if(litros==0):
          km+=litros
        elif(litros<0):
          negativos.append(km-litros)
  print("qtd l: %d" %litros)



#print("qtd l: %d" %litros)


if(passou==True):
  print("Lar Deivis lar")
else:
  if len(negativos) >= 1:
    print(negativos[0])
  else:
    print(km)