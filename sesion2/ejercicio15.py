'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio15.py
Autor: Cristell Molina Gomez
Action: Suma valores ingresados por teclado
'''
suma = 0
for f in range(10):
  valor = float(input("Ingrese valor :"))
  suma = suma + valor
print("La suma es " + str(suma))
promedio = suma / 10
print("El promedio es: "+str(promedio))
