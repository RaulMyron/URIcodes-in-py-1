while(1):
  qtdCasas = int(input())
  
  if qtdCasas == 0:
    break

  arrayTotal = [[0] * 3 for i in range(qtdCasas-1)] #3 colunas #qtdCasas linhas

  #ler tudo
  for i in range(qtdCasas-1): #para qtddecasas
    for j in range(2): #coluna 1 e 2
      arrayTotal[i][j] = input(split)

  for i in range(qtdCasas-1):
    qtdPessoas, qtdConsumida = map(int, input().split())
  