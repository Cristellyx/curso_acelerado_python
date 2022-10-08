'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio3.py
Autor: Cristell Molina Gomez
Action:Pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
extra = float(input("Introduce tus horas extra: "))
pago_extra = float(input("Introduce lo que cobras por hora extra: "))
paga = (horas * coste) + (extra * pago_extra)
print("Tu paga es", paga)