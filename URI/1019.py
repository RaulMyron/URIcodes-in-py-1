import math

N = int(input())
H = 0
M = 0

if N >= 3600:
  H = math.floor(N/3600)
  Hsegundos = H*3600

if H % 3600 != 0:
  N-=Hsegundos

if N >= 60:
  M = math.floor(N/60)
  Msegundos = M*60

if M % 60 != 0:
  N-=Msegundos

print("%d:%d:%d" %(H,M,N))