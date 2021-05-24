import re

def getNumber(entrada):
  x = re.findall("\d", entrada)
  sla = [str(x) for x in x]
  a_string = "".join(sla)
  return int(a_string)

print(getNumber("123 abc"))