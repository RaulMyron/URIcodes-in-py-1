def verificaMES(a):
  mes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  mesreturn = ''
  for i in range(13):
    if(x==i):
      mesreturn = mes[i-1]
    
  print(mesreturn)

x = float(input())

verificaMES(x)

