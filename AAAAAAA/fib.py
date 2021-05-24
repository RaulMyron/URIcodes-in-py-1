#from collections import Counter
#c = Counter()

def fibonacci(n):
  contador = [0] * n
  def fib(n):
    contador[n] += 1
    #c[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
  print(contador)

fibonacci(3)



