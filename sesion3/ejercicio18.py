'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio18.py
Autor: Cristell Molina Gomez
Action: Autorización por nombre
'''
personas_autorizadas = ["Alberto", "Carmen", "Cristell", "Hugo", "Lorena"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")