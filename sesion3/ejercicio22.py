'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio22.py
Autor: Cristell Molina Gomez
Action: Loteria
'''
lista = []
for f in range(5):
  numero = int(input("Introduce un numero ganador: "))
  lista += [numero]


lista.sort()
print("-------------------------------")
print("Los numeros ganadores son ")
for f in lista:
  print(f)