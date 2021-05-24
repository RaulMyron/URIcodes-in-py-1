def HoraseMinutos(Segundos):
  Horas = 0
  Minutos = 0
  while(Segundos>=3600):
    Horas+=1
    Segundos-=3600
  while(Segundos>=60):
    Minutos+=1
    Segundos-=60
  return(Horas, Minutos)

Hinicial, Minicial, Hfinal, Mfinal = map(float, input().split())

Si = (Hinicial*3600) + (Minicial*60)
Sf = (Hfinal*3600) + (Mfinal * 60)

if Si == Sf:
  print("O JOGO DUROU 24 HORA(S)")
elif Sf > Si:
  H, M = HoraseMinutos(Sf-Si)
  print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(H, M))
else:
  Tempo = (86400-Si) + Sf
  H, M = HoraseMinutos(Tempo)
  if(Si>Sf):
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(H, M))

