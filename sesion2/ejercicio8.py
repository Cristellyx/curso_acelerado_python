'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio8.py
Autor: ..............
Action: detecta numero negativos
'''
numero = int(input("Escriba un número: "))
if numero < 0:
  print("El numero "+ str(numero) +" es negativo")
elif numero == 0:
  print("El número es " + str(numero))
else:
  print("El numero "+str(numero) +" es positivo")