def stockmarket(lista_tuplas):
  stock_market = {}
  for i in tuple(lista_tuplas):
    if i[0] not in stock_market:
      stock_market[i[0]] = float(i[1] * i[2])
    else:
      stock_market[i[0]] += float(i[1] * i[2])
  return(stock_market)
	
stock = [('25-Out-2020', 40.0, 100, 'GM'),
('25-Out-2020', 42.0, 100, 'FIT'),
('01-Nov-2020', 36, 100, 'GM'),
('01-Nov-2020', 20, 100, 'FIT')]
print(stockmarket(stock))