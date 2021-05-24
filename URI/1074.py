def identifica(valor):
  maismenos=''
  parimpar=''
  if valor>0:
    maismenos='POSITIVE'
  elif valor<0:
    maismenos='NEGATIVE'
  if valor%2 == 0:
    parimpar='EVEN'
  else:
    parimpar='ODD'
  if valor == 0:
    return print('NULL')
  else: 
    return print("%s %s" %(parimpar,maismenos))

X = int(input())

for i in range(X):
  identifica(int(input()))

