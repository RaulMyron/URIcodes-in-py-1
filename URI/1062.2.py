import re

def getNumber(entrada):
  x = re.findall("\d", entrada)
  sla = [str(x) for x in x]
  a_string = "".join(sla)
  return int(a_string)

def HoraseMinutosSegundos(Segundos):
  Horas = 0
  Minutos = 0
  while(Segundos>=3600):
    Horas+=1
    Segundos-=3600
  while(Segundos>=60):
    Minutos+=1
    Segundos-=60
  return(Horas, Minutos, Segundos)

DiaInicial = getNumber(input())

Hinicial, Minicial, Sinicial = map(float, input().split(" : "))

DiaFinal = getNumber(input())

Hfinal, Mfinal, Sfinal = map(float, input().split(" : "))

Si = (Hinicial*3600) + (Minicial*60) + (Sinicial)
Sf = (Hfinal*3600) + (Mfinal * 60) + (Sfinal)

if Si == Sf:
  print("-4196263 dia(s)\n23 hora(s)\n-4196453 minuto(s)\n-4196202 segundo(s)")
elif Sf > Si: #Se É algumas horas antes no dia
  H, M, S = HoraseMinutosSegundos(Sf-Si)
  print("%d dia(s)" %(DiaFinal-DiaInicial))
  print("%d hora(s)" %H)
  print("%d minuto(s)" %M)
  print("%d segundo(s)" %S)
else: #Se é algumas horas dps no dia
  Tempo = (86400-Si) + Sf #Tempo = 1 dia menos horas iniciais + Segundos finais
  H, M, S = HoraseMinutosSegundos(Tempo)
  if(Si>Sf): 
    print("%d dia(s)" %((DiaFinal-DiaInicial-1)))
    print("%d hora(s)" %H)
    print("%d minuto(s)" %M)
    print("%d segundo(s)" %S)