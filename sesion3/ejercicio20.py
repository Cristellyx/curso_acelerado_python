'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio20.py
Autor: Cristell Molina Gomez
Action: Suma de precios
'''
total = 0
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]

for price in prices:
  total = total+price
  if price < min:
    min = price
  elif price > max:
    max = price

print("La suma total es "+ str(total))
print("El mínimo es " + str(min))
print("El máximo es " + str(max))