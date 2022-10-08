'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio16.py
Autor: Cristell Molina Gomez
Action: Imprime un triangulo
'''
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
  for j in range(i + 1):
    print("*", end="")
  print("")