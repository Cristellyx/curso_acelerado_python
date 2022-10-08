'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio27.py
Autor: Cristell Molina Gomez
Action: Directorio
'''
aux = ["Nombre","Edad","Direccion","Telefono"]
datos = {}

for f in aux:
  valor = input('Introduce el valor '+ f+': ')
  datos[f] = valor

print("---------------------------------")
print(datos["Nombre"]+" tiene "+datos["Edad"]+" años, vive en "+ datos["Direccion"]+" y su numero de telefono es "+ datos["Telefono"])
  
