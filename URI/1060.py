lista = []
for i in range(6):
  lista.append(float(input())) 
contador = 0
for i in range(6):
  if(lista[i]>0):
    contador += 1

print(contador, "valores positivos")