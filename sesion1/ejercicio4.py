'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio4.py
Autor: Cristell Molina Gomez
Action: Índice de masa corporal peso en kg/ estatura mtrs cuadrados
'''
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))