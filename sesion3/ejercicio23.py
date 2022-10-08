'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio23.py
Autor: Cristell Molina Gomez
Action: Producto escalar
'''

a = (1, 2, 3)
b = (-1, 0, 2)
c = (2, 1, 4)
product = 0
for i in range(len(a)):
  product += a[i]*b[i]*c[i]
print("El producto de los vectores" + str(a) +", "+str(b) + " y " + str(c) + " es " + str
(product))