# Sesion 2

---
Listado de ejercicios

* ejercicio8.py

Descripción:  Detecta numero negativos

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio8.py
Autor: Cristell Molina Gomez
Action: Detecta numero negativos
'''
numero = int(input("Escriba un número: "))
if numero < 0:
  print("El numero "+ str(numero) +" es negativo")
elif numero == 0:
  print("El número es " + str(numero))
else:
  print("El numero "+str(numero) +" es positivo")
```
<br>
<hr>

* ejercicio9.py

Descripción: Validar contraseña

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio9.py
Autor: Cristell Molina Gomez
Action: Validar contraseña
'''
password_correcta = "holaMundo"
password = input("Escriba la contaseña: ")

if password_correcta == password :
  print("La contraseña es correcta")

else:
  print("La contraseña es incorrecta")
```
<br>
<hr>

* ejercicio10.py

Descripción: Numero par o impar

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio10.py
Autor: Cristell Molina Gomez
Action: Numero par o impar
'''
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
  print("El número " + str(n) + " es par")
else:
  print("El número " + str(n) + " es impar")
```
<br>
<hr>

* ejercicio11.py

Descripción: Estructura condicional anidada

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio11.py
Autor: Cristell Molina Gomez
Action: Estructura condicional anidada
'''
mes = int(input("Introduzca el mes del año: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 :
  print("El mes tiene 31 días.")
elif mes == 2:
  print("El mes tiene 28 o 29 días.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  print("El mes tiene 30 días.")
else:
  print("Mes no válido.")

```
<br>
<hr>

* ejercicio12.py

Descripción: Estructura condicional anidada

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio12.py
Autor: Cristell Molina Gomez
Action: Estructura condicional anidada
'''
mes = int(input("Introduzca el mes de año: "))
if 1 <= mes <= 12:
  print("Se ha introducido un mes válido.")
else:
  print("El mes es incorrecto. Por defecto se elige Enero.")
  mes = 1

print("Se utilizará mes", mes)
```
<br>
<hr>

* ejercicio13.py

Descripción: Suma de 10 primeros numeros

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio13.py
Autor: Cristell Molina Gomez
Action: Suma de 10 primeros numeros
'''
num = 1
suma = 0
while num <= 10:
  suma += num
  print(suma)
  num += 1
```
<br>
<hr>

* ejercicio14.py

Descripción: Mostrar 10 veces un mensaje

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio14.py
Autor: Cristell Molina Gomez
Action: Mostrar 10 veces un mensaje
'''
num = 1
mensaje = input("Escriba un mensaje: ")
while num <= 10:
  print(str(num)+" "+mensaje)
  num += 1
```
<br>
<hr>

* ejercicio15.py

Descripción: Suma valores ingresados por teclado

```python
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
```
<br>
<hr>

* ejercicio16.py

Descripción: Imprime un triangulo

```python
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
```
<br>
<hr>

* ejercicio17.py

Descripción: Pedir número para tabla de multiplicar

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio17.py
Autor: Cristell Molina Gomez
Action: Pedir tabla de multiplicar
'''
numero = int(input("Introduce un numero (entero positivo): "))
for f in range(12):
  multi = numero * (f+1)
  print(str(numero) +" x "+str(f+1) + " = " + str(multi))
```
<br>
<hr>





