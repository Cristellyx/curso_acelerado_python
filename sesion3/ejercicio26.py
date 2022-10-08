'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio26.py
Autor: Cristell Molina Gomez
Action: Divisas
'''
divisas = {'Euro':'€', 'Dollar':'$', 'Peso':'$'}
ingresar = input('Introduce la divisa que desees conocer: ')
if ingresar in divisas:
  print(divisas[ingresar])
else:
  print("La divisa no esta en el diccionario")