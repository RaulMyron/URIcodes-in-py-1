N = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
qtdNOTAS = [0, 0, 0, 0, 0, 0, 0]

print(N)

for i in range(7):
    while N >= notas[i]:
      qtdNOTAS[i] += 1
      N -= notas[i]

for i in range(7):
    print("%d nota(s) de R$ %d,00" %(qtdNOTAS[i],notas[i] ))