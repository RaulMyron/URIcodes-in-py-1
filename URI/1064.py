lista = []
for i in range(6):
  lista.append(float(input())) 
contador = 0
pos = []
soma = 0
for i in range(6):
  if(lista[i]>0):
    pos.append([lista[i]])
    soma += lista[i]
    contador += 1
for i in pos:
  media = soma/len(pos)

print("%d valores positivos" %contador)
print("%.1f" %media)

