lista = []
for i in range(5):
  lista.append(float(input())) 
contador = 0
for i in range(5):
  if(lista[i]%2 == 0):
    contador += 1

print(contador, "valores pares")