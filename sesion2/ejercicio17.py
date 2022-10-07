'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio17.py
Autor: ..............
Action: Tabla de multiplicar
'''
numero = int(input("Introduce un numero (entero positivo): "))
for f in range(12):
  multi = numero * (f+1)
  print(str(numero) +" x "+str(f+1) + " = " + str(multi))