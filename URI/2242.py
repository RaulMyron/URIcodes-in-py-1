risada = str(input())
strV = ''
Vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(len(risada)):
  if Vogais.count(risada[i]) > 0 :
    strV += risada[i]

if strV == strV[::-1]:
    print("S")
else:
    print("N")