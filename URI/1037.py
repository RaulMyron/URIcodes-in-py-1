A, B = map(int, input().split())
Bb = 1 * B

if(B < 0):
  Bb = -B

R = A % Bb

if A%B != 0:
  Q = (A - R)/B
else:
  Q = A/Bb
  if (A and B) <= 0:
    Q = -Q

print("%d %d" %(Q, R))
