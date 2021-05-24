DIAS = int(input())
ANOS = 0
MES = 0

while DIAS >= 365:
  ANOS += 1
  DIAS -=365

while DIAS >= 30:
  MES += 1
  DIAS -= 30

	
print("%d ano(s)" %ANOS)
print("%d mes(es)" %MES)
print("%d dia(s)" %DIAS)