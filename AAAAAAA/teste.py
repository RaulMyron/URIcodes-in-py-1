K = int(input()) #1 0
L = int(input()) #2 1 
M = int(input()) #3 2
N = int(input()) #4 3
D = int(input()) #5 4

tupla = (K,L,M,N)

#index+4 1 
lista = []

for i in range(D):
  lista.append(0)

#print(lista)

o=0
if(K!=1):
  o = K-1

for k in tupla:
  n=0
  #print(lista)
  while(n<D):
    try:
      lista[(k-1)+n]+=1
      n+=4+o
    except IndexError:
      break

#print(lista)

tupla_lista = tuple(lista)
batidos = sum(list(tupla_lista)) 

print(batidos)