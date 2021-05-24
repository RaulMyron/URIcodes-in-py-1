DDD=[61, 71, 11, 21, 32, 19, 27, 31]
DDDcidades=["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

x = int(input())
z = DDD.index(x, 0, 7)
print(DDDcidades[z])

#funciona aqui, mas dá runtime error
