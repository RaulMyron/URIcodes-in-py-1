N = int(input())
Ni = N
qtd100 = 0
qtd50 = 0
qtd20 = 0
qtd10 = 0
qtd5 = 0
qtd2 = 0
qtd1 = 0

while (N >= 100):
    qtd100 += 1
    N -= 100

while (N >= 50):
    qtd50 += 1
    N -= 50

while (N >= 20):
    qtd20 += 1
    N -= 20

while (N >= 10):
    qtd10 += 1
    N -= 10

while (N >= 5):
    qtd5 += 1
    N -= 5

while (N >= 2):
    qtd2 += 1
    N -= 2

while (N >= 1):
    qtd1 += 1
    N -= 1

print(Ni)
print("%d nota(s) de R$ 100,00" % qtd100)
print("%d nota(s) de R$ 50,00" % qtd50)
print("%d nota(s) de R$ 20,00" % qtd20)
print("%d nota(s) de R$ 10,00" % qtd10)
print("%d nota(s) de R$ 5,00" % qtd5)
print("%d nota(s) de R$ 2,00" % qtd2)
print("%d nota(s) de R$ 1,00" % qtd1)
