X = int(input())
lista = []

contadorIn = 0
contadorOut = 0

for i in range(X):
  lista.append(int(input()))
    
for i in lista:
  if(i >= 10 and i <= 20):
    contadorIn += 1
  else:
    contadorOut += 1

print(contadorIn, "in")
print(contadorOut, "out")